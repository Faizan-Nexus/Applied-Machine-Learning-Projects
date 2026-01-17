import speedtest as st
import sys
from time import sleep

def progress_bar(progress, total, prefix=''):
    """Simple progress bar for visual feedback"""
    bar_length = 30
    filled_length = int(round(bar_length * progress / float(total)))
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r{prefix}[{bar}] {progress}/{total}')
    sys.stdout.flush()

def speed_test():
    """
    Performs an internet speed test and displays download speed, upload speed, and ping.
    Includes error handling and progress indicators.
    """
    try:
        print("Initializing speed test...")
        test = st.Speedtest()
        test.get_best_server()  # Get the best server for testing
        
        # Download speed test
        print("\nTesting download speed...")
        for i in range(1, 11):
            progress_bar(i, 10, 'Download: ')
            sleep(0.1)
        down = test.download()
        down = round(down / 10**6, 2)
        print(f"\nDownload Speed: {down} Mbps")
        
        # Upload speed test
        print("\nTesting upload speed...")
        for i in range(1, 11):
            progress_bar(i, 10, 'Upload: ')
            sleep(0.1)
        up = test.upload()
        up = round(up / 10**6, 2)
        print(f"\nUpload Speed: {up} Mbps")
        
        # Ping test
        print("\nMeasuring ping...")
        ping = test.results.ping
        print(f"Ping: {ping:.2f} ms")
        
        print("\n" + "="*40)
        print("Speed Test Results Summary:")
        print("="*40)
        print(f"Download Speed: {down} Mbps")
        print(f"Upload Speed: {up} Mbps")
        print(f"Ping: {ping:.2f} ms")
        print("="*40)
        
    except st.SpeedtestException as e:
        print(f"\nError during speed test: {str(e)}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    print("Starting Internet Speed Test...")
    speed_test()
