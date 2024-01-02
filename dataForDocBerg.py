
import csv

data = [

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

# ----------------- 


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


# ----------------


    {"Question": "What is DocBerg?", "Answer": "DocBerg is an ever-evolving platform committed to improving and updating based on user feedback and AI advancements."},
    {"Question": "What does DocBerg offer?", "Answer": "DocBerg offers services such as Listen Audio of PDF/Images, Chat Visualizer, Resume Analyzer, PDF conversion, and more."},
    {"Question": "What is Chat Visualizer?", "Answer": "Chat Visualizer provides profound insights about your chat with DocBerg's AI-powered tool."},
    {"Question": "What is Resume Analyzer?", "Answer": "Resume Analyzer offers profound insights about your Resume/CV with DocBerg's AI-powered tool."},
    {"Question": "What is PDF to Image?", "Answer": "PDF to Image converts your PDF documents into images with DocBerg."},
    {"Question": "What is Compress PDF?", "Answer": "Compress PDF allows you to compress your PDF documents using DocBerg."},
    {"Question": "What is Doc to PDF?", "Answer": "Doc to PDF converts Word Documents into PDF format with DocBerg."},
    {"Question": "What is Merge PDF?", "Answer": "Merge PDF allows you to select and merge multiple PDFs with DocBerg."},
    {"Question": "What is Image to PDF?", "Answer": "Image to PDF converts your images into PDF format with DocBerg."},
    {"Question": "What is PDF to Doc?", "Answer": "PDF to Doc converts PDF documents into Word Documents with DocBerg."},
    {"Question": "What is Compress Images?", "Answer": "Compress Images allows you to compress your images using DocBerg."},
    {"Question": "What is PNG to JPG?", "Answer": "PNG to JPG converts PNG images to JPG format with DocBerg."},
    {"Question": "What is JPG to PNG?", "Answer": "JPG to PNG converts JPG images to PNG format with DocBerg."},
    {"Question": "Tell me more about DocBerg features.", "Answer": "DocBerg features include Listen Audio of PDF/Images, Chat Visualizer, Resume Analyzer, PDF conversion, Compress PDF, Doc to PDF, Merge PDF, Image to PDF, PDF to Doc, Compress Images, PNG to JPG, and JPG to PNG."},
     {"Question": "Tell me features.", "Answer": "DocBerg features include Listen Audio of PDF/Images, Chat Visualizer, Resume Analyzer, PDF conversion, Compress PDF, Doc to PDF, Merge PDF, Image to PDF, PDF to Doc, Compress Images, PNG to JPG, and JPG to PNG."},
    


#     Greetings and General Questions



    {"Question": "Hello", "Answer": "Hi there! How can I help you with DocBerg today?"},
    {"Question": "Wassup", "Answer": "Not much! Just here to assist you with any questions about DocBerg."},
    {"Question": "What are you doing?", "Answer": "I'm here to provide information and answer your questions about DocBerg. How can I assist you?"},
    {"Question": "What are you doing?", "Answer": "I'm here to provide information and answer your questions about DocBerg. How can I assist you?"},


#   

{"Question": "Address", "Answer": "We are operating remotely "},
{"Question": "where to visit you", "Answer": "Mail us or Call us"}





]


# Rest of the code remains the same
csv_file_path = "docberg_qa.csv"
fieldnames = ["Question", "Answer"]

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write the data
    writer.writerows(data)

print(f"CSV file '{csv_file_path}' has been generated successfully.")