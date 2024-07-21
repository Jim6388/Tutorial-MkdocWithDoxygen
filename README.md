# Tutorial-MkdocWithDoxygen

Master C Documentation with MkDocs & Doxygen (using the stunning MkDocs Material theme)

This step-by-step tutorial empowers you to write professional technical documentation for your C projects. Learn how to leverage the power of MkDocs for clean and modern documentation websites, and Doxygen for automatic API reference generation.

## What you'll learn

- MkDocs Fundamentals and Material Theme: Set up MkDocs for building beautiful and user-friendly documentation using the Material theme.
- Doxygen Magic: Harness Doxygen to automatically generate detailed API reference from your C code comments.
- Combining Powers: Integrate MkDocs and Doxygen to create a seamless documentation workflow for your C projects.
- Bonus: Explore best practices for writing clear and concise technical documentation.

## Target Audience

- C Programmers (beginners or those looking to improve their documentation skills)
- Developers seeking to build well-documented C projects

## Things you need to know before getting start

This tutorial empowers you to craft professional C documentation with ease. We'll leverage two powerful tools:

- MkDocs Material: This popular theme is a powerful documentation framework on top of MkDocs. It allows you focus on the content of your documentation and create a professional static site in minutes. No need to know HTML, CSS or JavaScript – let Material for MkDocs do the heavy lifting for you
- Doxygen: This tool automates the creation of detailed API reference documentation from your C code comments, saving you significant time and effort.

### Our Unique Approach

While these tools are powerful, they don't natively integrate. This tutorial addresses this by using a custom Python script that bridges the gap between Doxygen and MkDocs Material. This script ensures seamless integration and a unified user experience for your C documentation.

Ready to build beautiful docs? The detailed guide awaits you in the next section.

## Let's Get Started: A Step-by-Step Tutorial for C Documentation

### Material for MkDocs

The first step is installing Material for MkDocs. Material for MkDocs is published as a Python package and can be installed with pip, ideally by using a virtual environment. Open up a terminal and install Material for MkDocs with:

```python
pip install mkdocs-material
```

Next, create a new MkDocs project:

```sh
mkdocs new .
```

This creates a basic project structure with a `mkdocs.yml` configuration file and a `docs` folder to store your documentation content.

```sh
.
├── docs
│   └── index.md
└── mkdocs.yml
```

Now, let's configure the project to use the Material theme. Open `mkdocs.yml` with your favorite editor and add the following lines:

```yaml
site_name: My site
site_url: https://mydomain.org/mysite
theme:
  name: material
```

These lines set the site name and URL (replace with your details) and enable the Material theme.

Congratulations! You've completed the basic configuration. To preview your documentation website locally, run the following command:

```sh
mkdocs serve
```

This starts a development server that allows you to view your documentation in a web browser (usually at http://127.0.0.1:8000/).

### Building Your Documentation Site

#### Customizing the Homepage

The `index.md` file located within the `docs` folder serves as the homepage for your documentation website. You can edit this file using your preferred Markdown editor to personalize the content and design of your homepage. This could involve adding introductory text, a project overview, or any information you want to showcase prominently.

#### Adding New Pages

To create additional pages for your documentation, simply create new Markdown files (`.md`) within the docs folder. Each new file will represent a separate page in your website's navigation. Use descriptive filenames and organize the files within subfolders if you have a large amount of content for better organization.

### Leveraging the Pre-configured mkdocs.yml

This tutorial provides a sample mkdocs.yml configuration file specifically tailored for C/C++ documentation in the c-project-docs folder. This configuration includes options that enhance the presentation of your technical content.

Here's how to integrate it into your project:

- Navigate to the `c-project-docs folder` and copy all the text within the `mkdocs.yml` file.
- Paste the copied content into your project's existing mkdocs.yml file. Remember to update the following sections with your project-specific details: site_name, site_author, site_url, copyright, etc..
- Copy the `mathjax.js` file from the `c-project-docs/docs/javascript` folder and paste it into the `docs/javascripts` directory within your MkDocs project.

Note:
> You could also check this [reference](https://squidfunk.github.io/mkdocs-material/reference/) if you want to have a deep dive about how to properly configure the options.

## Reference

[Material of Mkdoc official website](https://squidfunk.github.io/mkdocs-material/)
