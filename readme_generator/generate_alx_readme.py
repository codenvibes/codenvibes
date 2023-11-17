#!/usr/bin/python3
def generate_readme():
    project_number = input("Project Number: ")
    project_title = input("Project Title: ").upper()
    highlights = int(input("Number of highlights: "))
    resources_count = int(input("Number of Resources: "))
    objectives_count = int(input("Number of Objectives: "))
    question_count = int(input("Number of Questions: "))
    mandatory_task_count = int(input("Number of Mandatory Tasks: "))
    advanced_task_count = int(input("Number of Advanced Tasks: "))

    with open("README.md", "w") as readme:
        readme.write('<h1 align="center"><b>{}. {}</b></h1>\n'.format(project_number, project_title))

        if highlights > 0:
            highlight_section=  ""
            for _ in range(highlights):
                if _ == highlights - 1:
                    highlight_section += "<code></code>"
                else:
                    highlight_section += "<code></code> "
            readme.write('<div align="center">{}</div>\n'.format(highlight_section))

        readme.write("\n")

        readme.write("<!-- ## Background Context -->\n\n")

        if resources_count > 0:
            readme.write("## Resources\n")
            for _ in range(resources_count):
                readme.write('<details>\n<summary><b><a href=" "> </a></b></summary><br>\n\n\n<br><p align="center">※※※※※※※※※※※※</p><br>\n</details>\n\n\n')
            readme.write("\n<!-- **man or help:**\n- `` -->\n\n")

        if objectives_count > 0:
            readme.write("## Learning Objectives\n")
            for _ in range(objectives_count):
                readme.write("<details>\n")
                readme.write('<summary><b><a href=" "> </a></b></summary><br>\n\n\n')
                readme.write('<br><p align="center">※※※※※※※※※※※※</p><br>\n</details>\n\n\n')

        readme.write("## Requirements\n")
        readme.write("<!-- Add your requirements here -->\n\n")
        readme.write("<!-- ## More Info -->\n\n")

        if question_count > 0:
            readme.write("## Quiz questions\n")
            for _ in range(question_count):
                readme.write("<details>\n")
                readme.write("<summary><h3>Question {}</h3></summary>\n\n".format(_))
                readme.write("\n</details>\n\n")

        mt = 0
        at = 0

        if mandatory_task_count > 0:
            readme.write("## Tasks\n")
            for mt in range(mandatory_task_count):
                readme.write("<details>\n")
                readme.write("<summary>\n\n### {}. \n".format(mt))
                readme.write("`mandatory`\n\n")
                readme.write("File: []()\n")
                readme.write("</summary>\n\n\n</details>\n\n")

        if advanced_task_count > 0:
            if mandatory_task_count == 0:
                readme.write("## Tasks\n")
                for at in range(advanced_task_count):
                    readme.write("<details>\n")
                    readme.write("<summary>\n\n### {}. \n".format(at))
                    readme.write("`#advanced`\n\n")
                    readme.write("File: []()\n")
                    readme.write("</summary>\n\n\n</details>\n\n")
            else:
                for at in range(advanced_task_count):
                    readme.write("<details>\n")
                    readme.write("<summary>\n\n### {}. \n".format(at+mt+1))
                    readme.write("`#advanced`\n\n")
                    readme.write("File: []()\n")
                    readme.write("</summary>\n\n\n</details>\n\n")

if __name__ == "__main__":
    generate_readme()
