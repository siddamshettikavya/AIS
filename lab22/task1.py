class CustomerSupportChatbot:
    def __init__(self):
        self.supported_languages = {
            'en': {
                "greeting": "Hello! How can I help you today?",
                "farewell": "Goodbye! Have a nice day!",
                "unknown": "I'm sorry, I didn't understand that. Could you please rephrase?",
            },
            'es': {
                "greeting": "¡Hola! ¿En qué puedo ayudarte hoy?",
                "farewell": "¡Adiós! ¡Qué tenga un buen día!",
                "unknown": "Lo siento, no entendí eso. ¿Podrías reformularlo?",
            },
            'fr': {
                "greeting": "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
                "farewell": "Au revoir ! Passez une bonne journée !",
                "unknown": "Je suis désolé, je n'ai pas compris. Pourriez-vous reformuler ?",
            }
            # Add more languages as needed
        }
        self.default_language = 'en'
    
    def set_language(self, lang_code):
        if lang_code in self.supported_languages:
            self.default_language = lang_code
            return True
        return False

    def get_message(self, intent):
        return self.supported_languages[self.default_language].get(intent, self.supported_languages[self.default_language]["unknown"])

    def interact(self):
        print(self.get_message("greeting"))
        while True:
            user_input = input("> ")
            user_input_lower = user_input.strip().lower()
            if user_input_lower in ["bye", "adiós", "au revoir", "exit", "quit"]:
                print(self.get_message("farewell"))
                break
            elif "language" in user_input_lower:
                print("Please enter your language code (e.g., en, es, fr):")
                lang_code = input("> ").strip().lower()
                if self.set_language(lang_code):
                    print(f"Language set to {lang_code}.")
                else:
                    print("Sorry, that language is not supported.")
            else:
                # For demonstration, simple keyword matching
                if "help" in user_input_lower or "ayuda" in user_input_lower or "aide" in user_input_lower:
                    print(self.get_message("greeting"))
                else:
                    print(self.get_message("unknown"))

# --- Accessibility Testing Simulation ---

def test_accessibility_features():
    print("[Accessibility Feature Test]")
    # Simulate screen readers by always printing output text without special characters,
    # and by using descriptive labels.
    bot = CustomerSupportChatbot()
    print("Screen Reader Simulation: Greeting--- " + bot.get_message("greeting").replace("¡","").replace("!",""))
    # Test language switching for inclusivity
    assert bot.set_language('es')
    print("Screen Reader Simulation [Spanish]: Greeting--- " + bot.get_message("greeting").replace("¡","").replace("!",""))
    assert bot.set_language('fr')
    print("Screen Reader Simulation [French]: Greeting--- " + bot.get_message("greeting"))
    # Test fallback for unavailable language
    assert not bot.set_language('de')  # Not supported

if __name__ == "__main__":
    print("Launching Customer Support Chatbot Demo (Ctrl+C or type 'bye' to exit)...")
    chatbot = CustomerSupportChatbot()
    chatbot.interact()
    test_accessibility_features()

    # Discussion
    print("\n--- Discussion ---")
    print("Lack of inclusivity in AI, such as not supporting multiple languages or accessibility tools, can create digital inequality by excluding non-native speakers or users with disabilities from vital services.")
    print("Ethical approaches for accessibility include: supporting diverse languages, providing simple and clear responses, ensuring screen reader compatibility (using descriptive text), and continuously testing with users who have various needs.")

