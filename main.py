import req, ocr, ss, keyboard, os, time
from visual_comparison import ImageComparisonUtil


# using visual mismatch detection
if os.path.exists("old_ss.png"):
    os.remove("old_ss.png") # start from new
if os.path.exists("ss.png"):
    os.remove("ss.png")

try:
    while True:
        time.sleep(10)  # Wait for 10 seconds before the next cycle

        ss.capture_region_pil()
        new = ImageComparisonUtil.read_image("ss.png")
        prev_text = ""

        if os.path.exists("old_ss.png"):
            old = ImageComparisonUtil.read_image("old_ss.png")
            if ImageComparisonUtil.compare_images(old, new) < 0.97:
                print("Mismatch detected.")
                text = ocr.extractText(); # extract text from that ss
                print("Extracted text from old_ss.png:", prev_text)
                print("Extracted text from ss.png:", text)
                if text == "":
                    continue;
                if text == prev_text:
                    print("No new text detected. Skipping sending request.")
                    continue;
                if "eee" in text:
                    print("user is typing, skipping sending request.")
                    continue;
                reply = req.send_req(text); # sends the message to remote server with ollama on it
                if "error" in reply:
                    exit();

                keyboard.write(reply, delay=0.03)
                keyboard.press("enter")

                time.sleep(1)  # Wait for a second before taking the next screenshot
                ss.capture_region_pil()
                os.remove("old_ss.png")  # remove the old screenshotYay! Auto-cha
                os.rename("ss.png", "old_ss.png")
                # now if the person replies back with a new message then we will answer

                prev_text = text  # Store the previous text for comparison
            else:
                print("No mismatch detected.")
        else:
            print("No previous screenshot found. Saving current screenshot as old_ss.png.")
            os.rename("ss.png", "old_ss.png")

except KeyboardInterrupt:
    print("Stopped.")

