from logic1 import *


def main() -> None:
    """
    Main function for the entire project
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()