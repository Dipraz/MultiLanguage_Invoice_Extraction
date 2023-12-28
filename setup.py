from setuptools import setup, find_packages

setup(
    name="invoice-image-analysis-app",  # Replace with your desired app name
    version="0.1.0",  # Update as needed
    description="Extracts key information from invoice images using AI.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dipraz/MultiLanguage_invoice-image-analysis-app",  # Replace with your GitHub repository URL
    author="Your Name",  # Replace with your name
    author_email="dip07.raz@gmail.com",  # Replace with your email
    license="MIT",  # Specify your chosen license
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "google-generativeai",
    ],
    entry_points={
        "console_scripts": [
            "invoice-app=app:main",  # Replace "app" with your main app file name
        ]
    },
)
