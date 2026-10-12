CREATE DATABASE chatbot_db;
USE chatbot_db;

CREATE TABLE intents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    intent_name VARCHAR(100) UNIQUE
);

CREATE TABLE responses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    intent_id INT,
    response_text TEXT,
    FOREIGN KEY (intent_id) REFERENCES intents(id)
);

INSERT INTO intents (intent_name) VALUES
(1,'greeting'),
(2,'attendance'),
(3,'fees'),
(4,'motivation'),
(5,'thank'),
(6,'how_are_you'),
(7,'name'),
(8,'creator'),
(9,'study'),
(10,'college'),
(11,'sports'),
(12,'music'),
(13,'movie'),
(14,'food'),
(15,'health'),
(16,'exercise'),
(17,'sleep'),
(18,'stress'),
(19,'happy'),
(20,'sad'),
(21,'angry'),
(22,'bored'),
(23,'friend'),
(24,'family'),
(25,'morning'),
(26,'afternoon'),
(27,'evening'),
(28,'night'),
(29,'travel'),
(30,'programming'),
(31,'python'),
(32,'cpp'),
(33,'java'),
(34,'ai'),
(35,'machine_learning'),
(36,'project'),
(37,'quote'),
(38,'career'),
(39,'interview'),
(40,'resume'),
(41,'success'),
(42,'failure'),
(43,'confidence'),
(44,'productivity'),
(45,'focus'),
(46,'bye');

INSERT INTO responses (intent_id, response_text) VALUES

-- greeting
(1,'Hello! How can I help you?'),
(1,'Hi there! What can I do for you?'),

-- attendance
(2,'Attendance is marked automatically.'),
(2,'Attendance is updated daily.'),

-- fees
(3,'Please contact the accounts department.'),

-- motivation
(4,'Keep working hard and never give up.'),
(4,'Success comes with consistency.'),

-- thanks
(5,'You''re welcome!'),
(5,'Happy to help!'),
(5,'Anytime, glad I could assist.'),

-- how_are_you
(6,'I''m doing great.'),
(6,'I''m fine and ready to help.'),
(6,'Everything is working well.'),

-- name
(7,'I am your Python chatbot.'),
(7,'You can call me ChatBot.'),
(7,'I am a virtual assistant.'),

-- creator
(8,'I was created using Python.'),
(8,'A developer built me.'),
(8,'I was developed as a chatbot project.'),

-- study
(9,'Study consistently every day.'),
(9,'Focus on understanding concepts.'),
(9,'Practice makes learning easier.'),

-- college
(10,'College is a great place to learn.'),
(10,'Enjoy your college journey.'),
(10,'Keep improving your skills.'),

-- sports
(11,'Sports improve fitness.'),
(11,'Sports build teamwork.'),
(11,'Stay active and healthy.'),

-- music
(12,'Music helps people relax.'),
(12,'Music can improve mood.'),
(12,'Enjoy your favorite songs.'),

-- movie
(13,'Movies are great entertainment.'),
(13,'Try watching something inspiring.'),
(13,'Movies can be educational too.'),

-- food
(14,'Eat healthy and stay fit.'),
(14,'Balanced meals are important.'),
(14,'Don''t skip your meals.'),

-- health
(15,'Health is wealth.'),
(15,'Stay active every day.'),
(15,'Take care of your well-being.'),

-- exercise
(16,'Exercise regularly.'),
(16,'Stay physically active.'),
(16,'Fitness improves overall health.'),

-- sleep
(17,'Get enough sleep.'),
(17,'Rest is important.'),
(17,'Good sleep improves focus.'),

-- stress
(18,'Take breaks when needed.'),
(18,'Stay calm and positive.'),
(18,'Manage stress wisely.'),

-- happy
(19,'Glad to hear that!'),
(19,'Keep smiling.'),
(19,'Happiness is valuable.'),

-- sad
(20,'I hope things improve soon.'),
(20,'Stay strong.'),
(20,'Better days will come.'),

-- angry
(21,'Try to stay calm.'),
(21,'Take a deep breath.'),
(21,'Think before reacting.'),

-- bored
(22,'Try learning something new.'),
(22,'Read a book.'),
(22,'Explore a new hobby.'),

-- friend
(23,'Friends make life enjoyable.'),
(23,'Good friends are valuable.'),
(23,'Friendship matters.'),

-- family
(24,'Family is important.'),
(24,'Spend time with loved ones.'),
(24,'Family gives support.'),

-- morning
(25,'Good morning!'),
(25,'Have a productive day.'),
(25,'Wishing you a great morning.'),

-- afternoon
(26,'Good afternoon!'),
(26,'Hope your day is going well.'),
(26,'Have a pleasant afternoon.'),

-- evening
(27,'Good evening!'),
(27,'Enjoy your evening.'),
(27,'Hope you had a great day.'),

-- night
(28,'Good night!'),
(28,'Sleep well.'),
(28,'Sweet dreams.'),

-- travel
(29,'Travel safely.'),
(29,'Enjoy your journey.'),
(29,'Travel creates memories.'),

-- programming
(30,'Programming improves problem-solving.'),
(30,'Keep practicing coding.'),
(30,'Build projects to learn.'),

-- python
(31,'Python is beginner-friendly.'),
(31,'Python is popular for AI.'),
(31,'Python is versatile.'),

-- cpp
(32,'C++ is powerful.'),
(32,'C++ is great for DSA.'),
(32,'Practice C++ regularly.'),

-- java
(33,'Java is widely used.'),
(33,'Java supports OOP.'),
(33,'Java is powerful for applications.'),

-- ai
(34,'AI is transforming the world.'),
(34,'AI enables smart systems.'),
(34,'AI is an exciting field.'),

-- machine_learning
(35,'Machine Learning is part of AI.'),
(35,'ML learns from data.'),
(35,'ML powers many modern applications.'),

-- project
(36,'Projects build practical skills.'),
(36,'Projects strengthen your resume.'),
(36,'Keep working on innovative projects.'),

-- quote
(37,'Success comes from consistency.'),
(37,'Dream big and work hard.'),
(37,'Every expert was once a beginner.'),

-- career
(38,'Keep upgrading your skills.'),
(38,'Plan your career wisely.'),
(38,'Learning never stops.'),

-- interview
(39,'Prepare confidently.'),
(39,'Practice common questions.'),
(39,'Show your skills clearly.'),

-- resume
(40,'Keep your resume updated.'),
(40,'Highlight your projects.'),
(40,'Make your resume concise.'),

-- success
(41,'Success requires dedication.'),
(41,'Keep moving forward.'),
(41,'Consistency leads to success.'),

-- failure
(42,'Failure teaches lessons.'),
(42,'Never stop trying.'),
(42,'Learn and improve.'),

-- confidence
(43,'Believe in yourself.'),
(43,'Confidence grows with practice.'),
(43,'Trust your abilities.'),

-- productivity
(44,'Plan your tasks.'),
(44,'Avoid distractions.'),
(44,'Stay focused on priorities.'),

-- focus
(45,'Concentrate on one task at a time.'),
(45,'Remove distractions.'),
(45,'Stay committed to your goals.'),

-- bye
(46,'Good day 😊'),
(46,'Take care!'),
(46,'See you again soon!');