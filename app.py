import http.server
import socketserver
import gtts

# Set the port you want to use
port = 8080

# Create a custom request handler to serve HTML content and MP3 file


class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Chat Bot with Media Player</title>
            <style>
            body {
            font-family: Arial, sans-serif;
            }

            .chat-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            }

            .message {
            background-color: #f0f0f0;
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
            }

            .user-message {
            text-align: right;
            }

            .bot-message {
            text-align: left;
            }

            .media-player {
            margin: 10px 0;
            }
            .icon {
                text-align: center;
                margin-top: 20px;
            }

            .input-container {
                text-align: center;
                margin-top: 20px;
            }

            .user-input {
                width: 100%;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 5px;
                font-size: 16px;
            }
            </style>
            </head>
            <body>
            <div class="chat-container">
            <div class="message user-message">
            You: Hi There!
            </div>
            <div class="message bot-message">
            Bot:   Hi I am virtual agent . 
             <div class="icon">
            <img src="icon.png" alt="Icon" width="48" height="48">
             </div>
        
            <!-- User input text box -->
            <div class="input-container">
                <input type="text" class="user-input" placeholder="Type your message...">
                <button onclick="sendMessage()">Send</button>
            </div>
            <div class="media-player">
                <audio controls>
                    <source src="http://localhost:8080/hello.mp3" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
            </div>

            </div>
            <script>
            function sendMessage() {
                var userInput = document.querySelector(".user-input").value;
                var messageContainer = document.createElement("div");
                messageContainer.className = "message user-message";
                messageContainer.innerHTML = "You: " + userInput;
                document.querySelector(".chat-container").appendChild(messageContainer);
                document.querySelector(".user-input").value = "";
                 // Make an API call using fetch
                fetch("http://127.0.0.1/add", {
                    method: "POST", // Use GET or POST as per your API requirements
                    body: JSON.stringify({ message: userInput }),
                    headers: {
                        "Content-Type": "application/json"
                    }
                 })
            }
            </script>
            </body>
            </html>
            '''
            self.wfile.write(html_content.encode('utf-8'))
        elif self.path == '/hello.mp3':
            # tts = gtts.gTTS("Hi I am virtual agent . I am here 24/7 to help you with your travel plans to continue improve your experience, this conversation maybe recorded. If any point I am not able to assist you. I will connect you to an agent.")
            # tts.save("hello.mp3")
            self.send_response(200)
            self.send_header('Content-type', 'audio/mpeg')
            self.end_headers()
            with open('hello.mp3', 'rb') as mp3_file:
                self.wfile.write(mp3_file.read())
        elif self.path == '/hello.mp3':
            tts = gtts.gTTS("Hi I am virtual agent . I am here 24/7 to help you with your travel plans to continue improve your experience, this conversation maybe recorded. If any point I am not able to assist you. I will connect you to an agent.")
            tts.save("hello.mp3")
        else:
            super().do_GET()


# Create a socket server with the custom request handler
with socketserver.TCPServer(("", port), MyHandler) as httpd:
    print(f"Serving at port {port}")
    httpd.serve_forever()
