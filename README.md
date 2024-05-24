# HTTP Requests Tutorial

This project is a simple tutorial on how to make different types of HTTP requests.

## Features

- GET request to download a file
- HEAD request to get the headers of a resource
- PATCH request to partially update a resource
- OPTIONS request to get the allowed methods for a resource

## Usage

Open `index.html` in your web browser. You can click the buttons to make the different types of requests. The responses will be displayed below the buttons.

You can also use the provided `curl` commands to make the requests from the command line.

## Example `curl` Commands

- GET: `curl -X GET http://localhost:5000/download/filename -o filename`
- HEAD: `curl -I -X HEAD http://localhost:5000/resource`
- PATCH: `curl -X PATCH -H "Content-Type: application/json" -d '{"key":"new value"}' http://localhost:5000/resource`
- OPTIONS: `curl -I -X OPTIONS http://localhost:5000/resource`

## Note

The HEAD request only works with the `curl` command, not with the button in the browser.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)