from textblob import TextBlob

print("👋🎉 Welcome to Sentiment Spy 🕵️‍♂️")

user_name = input("Please enter your name: ").strip()

if not user_name:

   user_name = "Mystery Agent"

conversation_history = []

print(f"\nHello Agent {user_name}!")

print("Type a sentence and I will analyze your sentence with TextBlob 🔎")

print("Type 'reset', 'history', or 'exit' to quit.\n")

while True:

    user_input = input(">> ").strip()

    if not user_input:

        print("Please enter some text or a valid command.")

        continue

    if user_input.lower() == "exit":

        print(f"🚪 Exiting Sentiment Spy. Farewell Agent {user_name}!")

        break

    elif user_input.lower() == "reset":

        conversation_history.clear()

        print("🎉 All conversation history has been cleared!")

        continue

    elif user_input.lower() == "history":

        if not conversation_history:

            print("No conversation history yet.")

        else:

            print("\nConversation History:")

            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):

                if sentiment_type == "Positive":

                    emoji = "😃"

                elif sentiment_type == "Negative":

                    emoji = "😞"

                else:

                    emoji = "😑"

                    print(

                            f"{idx}. {emoji} {text} "

                            f"(Polarity: {polarity:.2f}, {sentiment_type})"

                        )

            continue

polarity = TextBlob(user_input).sentiment.polarity

if polarity > 0.25:

    sentiment_type = "Positive"

    emoji = "😃"

elif polarity < -0.25:

    sentiment_type = "Negative"

    emoji = "😞"

else:

    sentiment_type = "Neutral"

    emoji = "😑"

conversation_history.append((user_input, polarity, sentiment_type))

print(

f"{emoji} {sentiment_type} sentiment detected! "

f"(Polarity: {polarity:.2f})"

)