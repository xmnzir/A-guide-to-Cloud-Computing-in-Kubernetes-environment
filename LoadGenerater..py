import os
import time
import subprocess
import requests
from threading import Thread

class PerformanceTester:
    """ A program that tests the performance of JavaBenchmarkApp """

    def __init__(self, endpoint, rate):
        self.endpoint = endpoint
        self.rate = rate
        self.latencies = []
        self.error_count = 0
        self.stop_signal = False

    def check_connectivity(self):
        try:
            result = subprocess.run(['curl', '-s', self.endpoint],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                print("Curl connection successful. Response:")
                print(result.stdout)
            else:
                print("Curl connection failed. Error:")
                print(result.stderr)
        except Exception as e:
            print(f"Error during curl test: {e}")

    def make_request(self):
        try:
            response = requests.get(self.endpoint, timeout=20)
            if response.status_code == 200:
                response_text = response.text.strip()
                if response_text.startswith("Time:"):
                    time_ms = int(response_text.split(":")[1].strip().replace("ms", ""))
                    self.latencies.append(time_ms / 1000)
            else:
                self.error_count += 1
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
            self.error_count += 1

    def begin(self):
        self.check_connectivity()

        def worker():
            while not self.stop_signal:
                self.make_request()
                time.sleep(1 / self.rate)

        threads = []
        for _ in range(self.rate):
            thread = Thread(target=worker)
            thread.start()
            threads.append(thread)

        try:
            while not self.stop_signal:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nStopping load generator...")
            self.stop_signal = True
        finally:
            for thread in threads:
                thread.join()

    def generate_report(self):
        if self.latencies:
            avg_latency = sum(self.latencies) / len(self.latencies)
        else:
            avg_latency = 0
        print(f"Average Latency: {avg_latency:.2f}s")
        print(f"Error Count: {self.error_count}")


if __name__ == "__main__":
    endpoint = os.getenv("TARGET", "http://192.168.0.100:30000/primecheck")
    rate = int(os.getenv("FREQUENCY", "10"))
    print(f"Starting performance test for {endpoint} at {rate} requests/second...")

    tester = PerformanceTester(endpoint, rate)
    tester.begin()
    tester.generate_report()
