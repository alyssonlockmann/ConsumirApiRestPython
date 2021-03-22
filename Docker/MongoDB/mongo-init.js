db.auth('mongoadmin', 'adminpass')

db = db.getSiblingDB('pythonDb')

db.createCollection('pessoas')
db.createUser({
  user: 'pythonUser',
  pwd: 'pythonPass',
  roles: [
    {
      role: "readWrite", 
      db: "pythonDb"
    },
  ],
});