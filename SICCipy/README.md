# SICCiPy - Simple Internet Connection Checker

[Dishant Rathi](https://www.dishantrathi.tk)  [@techiedishant](https://www.twitter.com/techiedishant) 

A Simple Internet Connection Checker in python, wiz. used to check that, the machine on which the script is running has an Internet Connection or Not.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

```
git clone url
```

### Prerequisites

* [Python v3.6](https://www.python.org/) - As Base
* [Requests: HTTP for Humans](http://docs.python-requests.org/en/master/) - For HTTP Requests to check connectivity
* No Installation Required Just Clone and Run

## Running

To run the program, simply execute

* For Windows
    ```
    py SICCiPy.py
    ```
* For Linux
    ```
    python3 SICCiPy.py
    ```

### Concept Break down into parts

Explain "HOW" and "WHAT" these lines of code do ?

This code works on HTTP Response code {Default : 200}{May Change}, as shown in the image below the Response Code for [Google](https://www.google.com) is 200.

![Response Code](url)

Now if the response code is matched then it will show "Internet Enabled" else will pass and thows an exception "No Internet Connection : Check Your Lan | WiFi | Modem | Router Connections For More".

Try your self with an internet connection and by disabling wifi.{you will understand very well}

### Usage And Forks

Fork this repo and use in your block of code to check internet connection before running http requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details