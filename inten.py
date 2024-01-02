import csv
        
qa_pairs = [
    {"Question": "Hi there", "Answer": "Hello! Am Bot Here to help you."},
    {"Question": "How are you", "Answer": "Good to see you again! Am Bot Here to help you."},
    {"Question": "Is anyone there?", "Answer": "Hi there, how can I help?"},
    {"Question": "Hey", "Answer": "Hello! Am Bot Here to help you."},
    {"Question": "Hola", "Answer": "Hello! Am Bot Here to help you."},
    {"Question": "Hello", "Answer": "Hi there, how can I help?"},
    {"Question": "Good day", "Answer": "Hi there, how can I help?"},
    {"Question": "Bye", "Answer": "See you!"},
    {"Question": "See you later", "Answer": "Have a nice day"},
    {"Question": "Goodbye", "Answer": "Bye! Come back again soon."},
    {"Question": "Nice chatting to you, bye", "Answer": "Bye! Come back again soon."},
    {"Question": "Till next time", "Answer": "Bye! Come back again soon."},
    {"Question": "Thanks", "Answer": "My pleasure"},
    {"Question": "Thank you", "Answer": "You're Welcome"},
    {"Question": "That's helpful", "Answer": "You're Welcome"},
    {"Question": "Awesome, thanks", "Answer": "My pleasure"},
    {"Question": "Thanks for helping me", "Answer": "My pleasure"},
    {"Question": "What is Simplilearn?", "Answer": "Simplilearn is the popular online Bootcamp & online courses learning platform"},
    {"Question": "Tell me about interior design", "Answer": "Interior design involves creating aesthetically pleasing and functional spaces. Interior designers plan and execute designs for residential and commercial spaces."},
    {"Question": "What does an interior designer do?", "Answer": "Interior design involves creating aesthetically pleasing and functional spaces. Interior designers plan and execute designs for residential and commercial spaces."},
    {"Question": "Interior design services", "Answer": "Interior design involves creating aesthetically pleasing and functional spaces. Interior designers plan and execute designs for residential and commercial spaces."},
    {"Question": "Recommend a style for my living room", "Answer": "Sure! To recommend a style, I would need more information about your preferences. What colors, themes, or specific elements do you like?"},
    {"Question": "What interior style suits my space?", "Answer": "Sure! To recommend a style, I would need more information about your preferences. What colors, themes, or specific elements do you like?"},
    {"Question": "Living room design ideas", "Answer": "Sure! To recommend a style, I would need more information about your preferences. What colors, themes, or specific elements do you like?"},
    {"Question": "What colors work well in a bedroom?", "Answer": "Choosing bedroom colors depends on your preferences. Some popular choices include calming blues, soothing greens, or warm neutrals. What colors do you have in mind?"},
    {"Question": "Suggest bedroom color schemes", "Answer": "Choosing bedroom colors depends on your preferences. Some popular choices include calming blues, soothing greens, or warm neutrals. What colors do you have in mind?"},
    {"Question": "Favorite bedroom colors", "Answer": "Choosing bedroom colors depends on your preferences. Some popular choices include calming blues, soothing greens, or warm neutrals. What colors do you have in mind?"},
    {"Question": "What's the average cost of hiring an interior designer?", "Answer": "The cost varies based on factors like location, scope of work, and designer expertise. It's best to discuss your budget and requirements with a professional designer for accurate estimates."},
    {"Question": "Interior design budget", "Answer": "The cost varies based on factors like location, scope of work, and designer expertise. It's best to discuss your budget and requirements with a professional designer for accurate estimates."},
    {"Question": "Affordable interior design services", "Answer": "The cost varies based on factors like location, scope of work, and designer expertise. It's best to discuss your budget and requirements with a professional designer for accurate estimates."},
    {"Question": "Tell me about your design process", "Answer": "Our design process involves understanding your needs, creating conceptual designs, refining them based on your feedback, and finally implementing the approved design with attention to detail and quality."},
    {"Question": "How do you approach interior design?", "Answer": "Our design process involves understanding your needs, creating conceptual designs, refining them based on your feedback, and finally implementing the approved design with attention to detail and quality."},
    {"Question": "Design philosophy", "Answer": "Our design process involves understanding your needs, creating conceptual designs, refining them based on your feedback, and finally implementing the approved design with attention to detail and quality."},
    {"Question": "What is your contact number?", "Answer": "You can reach us at [Your Contact Number]. Feel free to call us or send an email to [Your Email Address] for inquiries or to schedule a consultation."},
    {"Question": "How can I reach you?", "Answer": "You can reach us at [Your Contact Number]. Feel free to call us or send an email to [Your Email Address] for inquiries or to schedule a consultation."},
    {"Question": "Contact information", "Answer": "You can reach us at [Your Contact Number]. Feel free to call us or send an email to [Your Email Address] for inquiries or to schedule a consultation."},
    {"Question": "Tell me about your services", "Answer": "We offer a range of services, including residential and commercial interior design, space planning, color consultation, and furniture selection. Our goal is to create spaces that reflect your style and meet your functional needs."},
    {"Question": "What services do you offer?", "Answer": "We offer a range of services, including residential and commercial interior design, space planning, color consultation, and furniture selection. Our goal is to create spaces that reflect your style and meet your functional needs."},
    {"Question": "Interior design offerings", "Answer": "We offer a range of services, including residential and commercial interior design, space planning, color consultation, and furniture selection. Our goal is to create spaces that reflect your style and meet your functional needs."},
    {"Question": "How are you?", "Answer": "I'm doing well, thank you! How can I assist you today?"},
    {"Question": "How are you doing?", "Answer": "I'm doing well, thank you! How can I assist you today?"},
    {"Question": "What’s up?", "Answer": "Not much, just here to help. How can I assist you?"},
    {"Question": "Good morning", "Answer": "Good morning! How can I help you today?"},
    {"Question": "Good evening", "Answer": "Good evening! How can I assist you today?"},
    {"Question": "Good afternoon", "Answer": "Good afternoon! How can I help you today?"},
    {"Question": "Good night", "Answer": "Good night! If you have any more questions, feel free to ask."},
    {"Question": "Tell me something", "Answer": "Certainly! What would you like to know?"},
    {"Question": "Ok", "Answer": "Okay! If you have any questions, feel free to ask."},
    {"Question": "Yes", "Answer": "Yes! How can I assist you today?"},
    {"Question": "I’ll do that now", "Answer": "Great! If you need any help along the way, feel free to ask."},
    {"Question": "Hello", "Answer": "Hello! Am Bot Here to help you."},
    {"Question": "Thank you", "Answer": "You're Welcome"},
    {"Question": "Goodbye", "Answer": "Bye! Come back again soon."},
    {"Question": "How can you help me?", "Answer": "I'm here to provide information and assistance. What do you need help with?"},
    {"Question": "What can you do?", "Answer": "I can answer questions, provide information, and assist with various tasks. Feel free to ask me anything."},
    {"Question": "Hi, my name is……", "Answer": "Hello [Your Name]! Nice to meet you. How can I assist you today?"},
    {"Question": "Happy birthday!", "Answer": "Thank you! If there's anything special you'd like to know or discuss, feel free to let me know."},
    {"Question": "I have a question", "Answer": "Sure, go ahead! I'm here to help."},
    {"Question": "Can you help me?", "Answer": "Of course! I'm here to assist you. What do you need help with?"},
    {"Question": "Are you human?", "Answer": "No, I'm not human. I'm a computer program designed to assist and provide information."},
    {"Question": "Are you a robot?", "Answer": "Yes, I am a virtual assistant powered by computer algorithms."},
    {"Question": "What is your name?", "Answer": "I don't have a personal name. You can call me ChatGPT."},
    {"Question": "How old are you?", "Answer": "I don't have an age. I'm a piece of software, and my development began in 2020."},
    {"Question": "What’s your age?", "Answer": "I don't age as I'm a computer program. My development began in 2020."},
    {"Question": "What day is it today?", "Answer": "I don't have real-time information, so I can't tell you the current day. Please check a calendar or your device for the current date."},
    {"Question": "What do you do with my data?", "Answer": "I don't process personal data unless explicitly provided for the purpose of the conversation. I prioritize user privacy and confidentiality."},
    {"Question": "Do you save what I say?", "Answer": "I don't retain personal data from our conversations. Your privacy and data security are important."},
    {"Question": "Who made you?", "Answer": "I was created by OpenAI, a research organization focused on artificial intelligence."},
    {"Question": "Which languages can you speak?", "Answer": "I can understand and generate text in multiple languages, including English."},
    {"Question": "What is your mother’s name?", "Answer": "I don't have a mother or family. I'm a computer program."},
    {"Question": "Where do you live?", "Answer": "I exist in the digital realm and don't have a physical location."},
    {"Question": "How many people can you speak to at once?", "Answer": "I can interact with many users simultaneously, but each conversation is separate and doesn't influence others."},
 
    {"Question": "Do you have a job for me?", "Answer": "I don't have the capability to offer employment. You might want to check job boards or company websites for job opportunities."},
    {"Question": "Where can I apply?", "Answer": "To apply for a job, visit the career page of the company you're interested in or use job search platforms."},
    {"Question": "Are you expensive?", "Answer": "I'm a free virtual assistant provided for informational purposes. There is no cost associated with using my services."},
    {"Question": "Who’s your boss / master?", "Answer": "I don't have a boss or master. I operate based on algorithms and programming."},
    {"Question": "Do you get smarter?", "Answer": "I don't inherently get smarter on my own. My performance improves as developers at OpenAI make updates to my underlying algorithms."},
 {"Question": "Address ", "Answer": "Delhi Laxmi Interior is located near [Include Specific Location Details]. For more precise directions, you may want to use a map or contact them directly."},
{"Question": "where to visit you", "Answer": "Delhi Laxmi Interior is located near [Include Specific Location Details]. For more precise directions, you may want to use a map or contact them directly."}

]

csv_file_path = "qa_pairs.csv"

# Writing to CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["Question", "Answer"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for pair in qa_pairs:
        writer.writerow(pair)

print(f"CSV file '{csv_file_path}' created successfully.")
