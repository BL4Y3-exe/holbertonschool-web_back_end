const fs = require('fs');
const http = require('http');

const database = process.argv[2];

function getStudents(path) {
  return fs.promises
    .readFile(path, 'utf8')
    .then((data) => {
      const lines = data.trim().split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};
      const output = [`Number of students: ${students.length}`];

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        output.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });

      return output.join('\n');
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

const app = http.createServer((request, response) => {
  response.writeHead(200, { 'Content-Type': 'text/plain' });

  if (request.url === '/students') {
    getStudents(database)
      .then((students) => {
        response.end(`This is the list of our students\n${students}\n`);
      })
      .catch((error) => {
        response.end(`This is the list of our students\n${error.message}\n`);
      });
  } else {
    response.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
