
from time import sleep
import board
import digitalio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont
import paho.mqtt.client as mqtt
from gpiozero import LED

red = LED(21)
yellow = LED(20)
green = LED(16)

def on_connect(client, userdata, flags, rc):
   # print("Connected with result code "+str(rc))
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
        client.subscribe("raspberry_mood")
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
   # message =(m5sg.topic+" "+str(msg.payload))
     # Define the Reset Pin
        oled_reset = digitalio.DigitalInOut(board.D4)

        # Change these
        # to the right size for your display!
        WIDTH = 128
        HEIGHT = 32  # Change to 64 if needed
        BORDER = 5

        # Use for I2C.
        #i2c = board.I2C()
        #oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

        # Use for SPI
        spi = board.SPI()
        oled_cs = digitalio.DigitalInOut(board.D5)
        oled_dc = digitalio.DigitalInOut(board.D6)
        oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

        # Clear display.
        oled.fill(0)
        oled.show()

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (oled.width, oled.height))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a white background
        draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

        # Draw a smaller inner rectangle
        draw.rectangle(
            (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
            outline=0,
            fill=0,
        )

         # Load default font.
        font = ImageFont.load_default()

        # Draw Some Text
        #text = "Hej guys, it's working!!!! :D"
        text = str(msg.payload)[2:-1]
        (font_width, font_height) = font.getsize(text)
        draw.text(
            (oled.width // 2 - font_width // 2, oled.height // 2 - font_height // 2),
            text,
            font=font,
            fill=255,
        )

        #variable to wait for new input:
        previous_message = str(msg.payload)[2:-1]

         # Display image
        if text == previous_message:
                 if "meh mood" in text:
                      yellow.on()
                      red.off()
                      green.off()
                 elif "good mood" in text:
                      green.on()
                      red.off()
                      yellow.off()
                 elif "sad mood" in text:
                      red.on()
                      green.off()
                      yellow.off()
                 elif "not in any mood" in text:
                      red.off()
                      green.off()
                      yellow.off()
                 else:
                      green.off()
                      yellow.off()
                      red.off()
                 for n in range(128,-128,-1):  #these numbers should be calculated by the width $
                        draw.text(
                                (n, oled.height // 2 - font_height //2),
                                text,
                                font=font,
                                fill=255,
                        )

                        #Display image
                        oled.image(image)
                        oled.show()
                        sleep(0.01)
                        draw.rectangle( #delete innermost area
                                (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER -$
                                outline=0,
                                fill=0,
                        )
                        previous_message = text

        else:
                # Create blank image for drawing.
                # Make sure to create image with mode '1' for 1-bit color.
                image = Image.new("1", (oled.width, oled.height))

                # Get drawing object to draw on image.
                draw = ImageDraw.Draw(image)

                # Draw a white background
                draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

                # Draw a smaller inner rectangle
                draw.rectangle(
                    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
                    outline=0,
                    fill=0,
                )

                for n in range(128,-128,-1):  #these numbers should be calculated by the width o$
                        draw.text(
                                (n, oled.height // 2 - font_height //2),
                                text,
                                font=font,
                                fill=255,
                        )
                        #Display image
                        oled.image(image)
                        oled.show()
                        sleep(0.01)
                        draw.rectangle( #delete innermost area
                                (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER -$
                                outline=0,
                                fill=0,
                        )
                        previous_message = text


    #if "moodboard mode" in message:
    #    client.unsubscribe("raspberry_kh")
    #if "chat mode" in message:
    #    client.subscribe("raspberry_kh")
                if "meh mood" in text:
                        yellow.on()
                        red.off()
                        green.off()
                elif "good mood" in text:
                        green.on()
                        red.off()
                        yellow.off()
                elif "sad mood" in text:
                        red.on()
                        green.off()
                        yellow.off()
                elif "not in any mood" in text:
                        red.off()
                        green.off()
                        yellow.off()




def mood():
                username = input("What's your name? ")
                client = mqtt.Client()
                client.on_connect = on_connect
                client.on_message = on_message
                client.subscribe("raspberry_mood")
                client.connect("test.mosquitto.org", 1883, 60)
                client.loop_start()
                #publish messages:
                try:
                                while True:
                                                value = input("Enter your message: ")
                                                client.publish("raspberry_mood", username + ": "$
                                                pass
                except KeyboardInterrupt:
                                client.disconnect()
                                client.loop_stop()

if __name__ == '__main__':
    mood()

