import fs from 'fs';

function readDatabase(path) {
  return fs.promises.readFile(path, 'utf8').then((data) => {
    const lines = data.trim().split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);
    const fields = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
    });

    return fields;
  });
}

export default readDatabase;
