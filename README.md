# AirBnB Clone Project - README

Welcome to the AirBnB Clone Project, the first step towards building a full web application inspired by the AirBnB platform. In this initial phase, we've created a command-line interface (CLI) that allows you to manage AirBnB objects. The CLI is designed to provide a foundation for upcoming features, including HTML/CSS templating, database storage, API integration, and front-end development.

## Display Image
![display image](PriviewImages/airbnbclone.png)

## Getting Started

To get started with the AirBnB clone project, follow these instructions:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd <project-directory>
   ```

3. Start the command interpreter using `./console.py`:

   ```bash
   ./console.py
   ```

This will launch the AirBnB console, which will display a prompt `(hbnb)`.

## Using the Console

The AirBnB console can be run in both interactive and non-interactive modes. In the interactive mode, you can enter commands and see the results immediately. In the non-interactive mode, you can pass a script with predefined commands.

Here's how to use the console in interactive mode:

```bash
AirBnB$ ./console.py
(hbnb) help
```

You'll see a list of documented commands and their descriptions. You can type any of these commands to interact with the program.

### Available Commands

- `EOF`: Exit the console.
- `help <topic>`: Get help on a specific command or topic.
- `quit`: Exit the program.

For example, to get help on the `quit` command, you can type:

```bash
(hbnb) help quit
```

This command interpreter allows you to perform various tasks, including creating new objects, retrieving objects from files or databases, performing operations on objects, updating attributes, and deleting objects.

## Project Structure

This project is organized around the following key objectives:

1. **BaseModel Class**: We have a parent class called `BaseModel`, which takes care of the initialization, serialization, and deserialization of future instances.

2. **Serialization/Deserialization**: We have established a simple flow of serialization and deserialization: `Instance <-> Dictionary <-> JSON String <-> File`. This allows us to save and load objects easily.

3. **AirBnB Classes**: We've created specific classes for various AirBnB objects, such as User, State, City, and Place, all of which inherit from the `BaseModel`.

4. **File Storage**: We've implemented an abstracted storage engine known as "File storage." This engine handles the saving and loading of objects to and from files.

5. **Unit Testing**: We've developed unit tests to validate the functionality of our classes and storage engine, ensuring they work as expected.

## What's a Command Interpreter?

The AirBnB command interpreter is a specialized command-line interface that allows you to manage objects within the AirBnB project. It's similar to a regular shell, but it is tailored to the specific use-case of managing AirBnB objects. With this interpreter, you can:

- Create new objects (e.g., Users, Places).
- Retrieve objects from files, databases, or other sources.
- Perform operations on objects, such as counting and computing statistics.
- Update attributes of objects.
- Delete (destroy) objects.

This command interpreter is the backbone of your AirBnB clone project and is a crucial tool for managing your application's data.

## Contribute

Feel free to contribute to this project by submitting issues, feature requests, or pull requests. We welcome collaboration from the open-source community to enhance and improve the AirBnB Clone project.

## Credits

This is a team project developed by Cyril Ondanje & Kidiavayi Omeno as part of the coursework at ALX SOFTWARE ENGINEERING bootcamp. We extend our gratitude to the open-source community for their contributions and support.

Happy coding!
