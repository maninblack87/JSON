var age = 39;
console.log('age = ' + JSON.stringify(age) + '\n');

var fullName = 'Larson Richard';
console.log('fullName = ' + JSON.stringify(fullName) + '\n');

var tags = ['json', 'rest', 'api', 'oauth'];
console.log('tags = ' + JSON.stringify(tags) + '\n');

var registered = true;
console.log('registered = ' + JSON.stringify(registered) + '\n');


var speaker = {
    firstName: 'Larson',
    lastName: 'Richard',
    email: 'larsonrichard@ecratic.com',
    about: 'Incididunt mollit cupidatat magna excepteur do tmpor ex non ...',
    company: 'Ecratic',
    tags: ['json', 'rest', 'api', 'oauth'],
    registered: true
};

console.log('speaker = ' + JSON.stringify(speaker));


function serializeSpeaker(key, value) {
    return (typeof value === 'string' || Array.isArray(value)) ? undefined : value;
}

console.log('speaker (pretty print):\n' + JSON.stringify(speaker, null, 2) + '\n');

console.log('speaker without String and Arrays:\n' + JSON.stringify(speaker, serializeSpeaker, 2));