# ImageUpscaler

Transform your low-resolution images into stunning high-quality masterpieces (4x upscaling) with ease using our Flask web application. Powered by AI image upscaling technology, it effortlessly enhances the details and sharpness of your images. Elevate your visual content and impress your audience with every click.

![ImageUpscaler](image.png "Elevate your low-res images effortlessly with our Flask web app powered by AI image upscaling.")

## Features

* **4x Upscaling:** Increase the resolution of your images by a factor of four.
* **AI-Powered:** Utilizes a pre-trained ESRGAN (Enhanced Super-Resolution Generative Adversarial Networks) model for high-quality results.
* **Web-Based Interface:** Easy-to-use web interface for uploading and enhancing images.
* **Fast and Efficient:** Quickly process your images and see the results in seconds.

## How It Works

This application is built with **Flask**, a lightweight web framework for Python. When you upload an image, it's processed by a pre-trained **ESRGAN model** loaded via **TensorFlow Hub**. The model upscales the image, and the enhanced version is then displayed back to you in the browser.

## Installation and Usage

To run this application on your local machine, please follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/g4m3r0/imageupscaler.git
    cd imageupscaler
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python app.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000` to use the application.

## Dependencies

The project's dependencies are listed in the `requirements.txt` file and include:
* Flask
* Pillow
* numpy
* tensorflow
* keras
* protobuf
* opencv_python
* tensorflow_hub

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information on how to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Useful Links

* [GSoftwareLab](https://gsoftwarelab.com)
* [Organic Website Traffic Bot](https://gsoftwarelab.com/organic-website-traffic-bot/)
* [ScrapingDuck - Web Scraping API](https://scrapingduck.com)
* [TheFastHost - Fast and Cheap Hosting](https://thefasthost.net)
