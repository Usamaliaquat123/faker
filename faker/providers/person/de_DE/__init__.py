# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}',
        '{{first_name_male}} {{last_name}}-{{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{first_name_female}} {{last_name}}-{{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
        '{{first_name_male}} {{last_name}} {{suffix}}',
        '{{first_name_female}} {{last_name}} {{suffix}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}} {{suffix}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}} {{suffix}}',
    )

    first_names_male = (
        'Abel', 'Abraham', 'Adalbero', 'Adam', 'Adamo', 'Adolfo', 'Adrian',
        'Adriano', 'Adrianus', 'Adrien', 'Alain', 'Alajos', 'Alan', 'Albain',
        'Alban', 'Albano', 'Alberto', 'Albin', 'Alec', 'Alejandro',
        'Alessandro', 'Alessio', 'Alex', 'Alexander', 'Alexandre',
        'Alexandros', 'Alexej', 'Alexis', 'Alfons', 'Alfonso', 'Aljoscha',
        'Allan', 'Allen', 'Alois', 'Alon', 'Alonzo', 'Alphonse', 'Alwin',
        'Amadeo', 'Amadeus', 'Amandus', 'Amos', 'Anatol', 'Anatole',
        'Anatolij', 'Anders', 'Andi', 'Andor', 'Andre', 'Andreas', 'Andrej',
        'Andrew', 'Andrijan', 'Andy', 'Angelus', 'Ansgar', 'Anthony',
        'Antoine', 'Anton', 'Antonio', 'Araldo', 'Aram', 'Argus', 'Arjan',
        'Armin', 'Arminio', 'Arnaldo', 'Arnault', 'Arndt', 'Arne', 'Arno',
        'Arnold', 'Arrigo', 'Art', 'Arthur', 'Artur', 'Arturo', 'August',
        'Auguste', 'Augustin', 'Aurelius', 'Axel', 'Balduin', 'Balthasar',
        'Bardo', 'Barnabas', 'Barnard', 'Barney', 'Baruch', 'Basil',
        'Basilius', 'Bastian', 'Bastien', 'Battista', 'Beatus', 'Beltrame',
        'Beltran', 'Ben', 'Benedetto', 'Benedict', 'Benedikt', 'Bengt',
        'Beniamino', 'Benignus', 'Benito', 'Benjamin', 'Benjy', 'Bennett',
        'Benno', 'Benny', 'Benoit', 'Beppe', 'Bernard', 'Bernardo', 'Bernd',
        'Bernhard', 'Bernie', 'Bert', 'Berthold', 'Bertoldo', 'Bertram',
        'Bertrame', 'Bill', 'Billy', 'Birger', 'Bjarne', 'Björn', 'Bob',
        'Bobby', 'Bodo', 'Bonifatius', 'Boris', 'Bosco', 'Brendan', 'Brian',
        'Bruno', 'Bryan', 'Burkhard', 'Camillo', 'Camilo', 'Carl', 'Carlo',
        'Carlos', 'Carol', 'Carsten', 'Casimir', 'Caspar', 'Cecil', 'Ceddric',
        'Cedric', 'Celestino', 'Charles', 'Charlie', 'Chico', 'Chip', 'Chris',
        'Christian', 'Christoph', 'Christophe', 'Christopher', 'Christy',
        'Chuck', 'Cian', 'Cillian', 'Clarence', 'Clark', 'Clas', 'Claude',
        'Claudio', 'Claudius', 'Claus', 'Clayton', 'Clemens', 'Cliff',
        'Clifford', 'Clint', 'Clinton', 'Cody', 'Colin', 'Collin', 'Conan',
        'Connor', 'Conny', 'Conor', 'Conrad', 'Constantine', 'Cooper',
        'Cordell', 'Cornelius', 'Corvinus', 'Cristobal', 'Curd', 'Curt',
        'Curtis', 'Curtiz', 'Cyril', 'Cyrill', 'Cäsar', 'Damian', 'Damon',
        'Dan', 'Daniel', 'Daniele', 'Danilo', 'Danny', 'Dario', 'Darius',
        'Dave', 'David', 'Davide', 'Dawson', 'Dean', 'Demetrius', 'Denis',
        'Deniz', 'Dennis', 'Derek', 'Desiderius', 'Detlef', 'Detlev', 'Dick',
        'Diego', 'Dieter', 'Dimitrij', 'Dirk', 'Dolf', 'Domenico', 'Domingo',
        'Dominic', 'Dominik', 'Dominikus', 'Dominique', 'Donald', 'Donatello',
        'Donato', 'Donatus', 'Dorian', 'Douglas', 'Dragan', 'Duarte', 'Duncan',
        'Dylan', 'Earnest', 'Earvin', 'Eike', 'Eleasar', 'Elia', 'Elian',
        'Elias', 'Elijah', 'Ellison', 'Elmar', 'Elroy', 'Emanuel', 'Emanuele',
        'Emil', 'Emile', 'Emilian', 'Emiliano', 'Emilio', 'Emmanuel', 'Endrik',
        'Enrico', 'Enrique', 'Enzo', 'Ephraim', 'Erasmus', 'Eric', 'Erik',
        'Ermanno', 'Ernest', 'Ernestin', 'Ernesto', 'Eros', 'Errol', 'Etienne',
        'Eugen', 'Eugene', 'Eugenio', 'Eusebius', 'Everett', 'Ezra', 'Fabiano',
        'Fabien', 'Fabio', 'Fabius', 'Fabrice', 'Fabricius', 'Fabrizio',
        'Falco', 'Falk', 'Falko', 'Faruk', 'Faustus', 'Favian', 'Federico',
        'Federigo', 'Fedor', 'Felice', 'Feliciano', 'Felicien', 'Felipe',
        'Felix', 'Felton', 'Feodor', 'Ferdinand', 'Fergus', 'Fernand',
        'Fernando', 'Ferrante', 'Ferris', 'Fidel', 'Fidelio', 'Fidelis',
        'Fidelius', 'Filippo', 'Finan', 'Finn', 'Fiore', 'Fjodor', 'Flavian',
        'Flemming', 'Fletcher', 'Flint', 'Florens', 'Florentin', 'Florian',
        'Florin', 'Florus', 'Floyd', 'Forrest', 'Forrester', 'Forster',
        'Foster', 'Fox', 'Francesco', 'Francis', 'Francisco', 'Franco',
        'Francois', 'Franek', 'Frank', 'Frankie', 'Franklin', 'Franziskus',
        'Frasier', 'Frayne', 'Fred', 'Freddy', 'Frederic', 'Frederick',
        'Frederik', 'Freeman', 'Fremont', 'Fridericus', 'Fridolin', 'Friedel',
        'Frye', 'Gabriel', 'Gaetan', 'Gaetano', 'Gallus', 'Garcia', 'Garfield',
        'Garin', 'Garnier', 'Garrick', 'Garrison', 'Garron', 'Garry', 'Garson',
        'Gaspar', 'Gaspard', 'Gaspare', 'Gaston', 'Gastonne', 'Gates',
        'Gauthier', 'Gavin', 'Gene', 'Geoffrey', 'Geoffroy', 'Geordi', 'Georg',
        'George', 'Georges', 'Gerald', 'Geraldo', 'Gerard', 'Geraud', 'Gerd',
        'Gereon', 'Germain', 'German', 'Germano', 'Gernot', 'Gerold',
        'Geronimo', 'Gerrit', 'Gerry', 'Gert', 'Gerulf', 'Gerwin', 'Giacomo',
        'Gian', 'Giancarlo', 'Gianni', 'Gibson', 'Gideon', 'Gil', 'Gilbert',
        'Gilberto', 'Gilles', 'Gillian', 'Gino', 'Gioacchino', 'Giorgio',
        'Giovanni', 'Giraldo', 'Gisbert', 'Gitano', 'Giuliano', 'Giulio',
        'Giuseppe', 'Giusto', 'Glen', 'Glenn', 'Goliath', 'Goran', 'Gordon',
        'Gordy', 'Goswin', 'Graciano', 'Graham', 'Grayson', 'Greg', 'Gregg',
        'Gregoire', 'Gregor', 'Gregory', 'Griffin', 'Grover', 'Gualtier',
        'Gualtiero', 'Guglielmo', 'Guido', 'Guillaume', 'Guillermo', 'Gunnar',
        'Gunter', 'Gunther', 'Gus', 'Gustavo', 'Gustl', 'Gutierre', 'Guy',
        'Götz', 'Günter', 'Günther', 'Hajo', 'Hamilton', 'Hamlet', 'Hampton',
        'Hanley', 'Hannes', 'Hans', 'Harald', 'Hardy', 'Harley', 'Harlow',
        'Harold', 'Haroun', 'Harrison', 'Harry', 'Harvey', 'Hasso', 'Hauke',
        'Havel', 'Hector', 'Heiko', 'Heiner', 'Heino', 'Hektor', 'Helge',
        'Helmut', 'Helmuth', 'Hendrick', 'Hendrik', 'Hennes', 'Henning',
        'Henri', 'Henrick', 'Henrik', 'Henry', 'Herald', 'Herbie', 'Hercules',
        'Herold', 'Herwig', 'Hieronymus', 'Hilarius', 'Holger', 'Holm',
        'Homer', 'Horace', 'Horatio', 'Horaz', 'Howard', 'Howie', 'Hugh',
        'Hugo', 'Humphrey', 'Hunter', 'Ignatius', 'Ignaz', 'Ignazio', 'Igor',
        'Ilian', 'Ilja', 'Immanuel', 'Ingo', 'Ingolf', 'Ingvar', 'Irenäus',
        'Irvin', 'Irving', 'Irwin', 'Isaac', 'Isaak', 'Isai', 'Isaiah',
        'Isidor', 'Istvan', 'Ivan', 'Ivo', 'Jackson', 'Jacky', 'Jacob',
        'Jacques', 'Jacquin', 'Jadon', 'Jago', 'Jaime', 'Jake', 'Jakob',
        'Jamal', 'James', 'Jan', 'Janis', 'Jannes', 'Jannik', 'Janning',
        'Janos', 'Janosch', 'Jaques', 'Jared', 'Jarik', 'Jarl', 'Jarno',
        'Jaro', 'Jaromir', 'Jarrett', 'Jascha', 'Jason', 'Jasper', 'Jay',
        'Jean', 'Jeff', 'Jefferson', 'Jeffrey', 'Jendrick', 'Jens', 'Jered',
        'Jeremiah', 'Jeremias', 'Jeremie', 'Jeremy', 'Jerold', 'Jerom',
        'Jerome', 'Jerrick', 'Jerry', 'Jesaja', 'Jesko', 'Jesse', 'Jim',
        'Jimmy', 'Jirko', 'Jo', 'Joakim', 'Joao', 'Joaquin', 'Joe', 'Joel',
        'Joey', 'John', 'Johnny', 'Jokim', 'Jonah', 'Jonas', 'Jonathan',
        'Jonny', 'Jordan', 'Jordano', 'Jorge', 'Jose', 'Josef', 'Joseph',
        'Josh', 'Joshua', 'Josias', 'Jost', 'Josua', 'Josue', 'Jourdain',
        'Juan', 'Juanito', 'Jud', 'Jules', 'Julien', 'Julio', 'Julius',
        'Jurij', 'Justin', 'Justinian', 'Justus', 'Jörg', 'Jürgen', 'Kain',
        'Kaj', 'Kajetan', 'Kallistus', 'Karsten', 'Kasimir', 'Kaspar',
        'Keamon', 'Keith', 'Ken', 'Kenan', 'Kenneth', 'Keno', 'Kersten',
        'Kerwin', 'Kevin', 'Kian', 'Kilian', 'Kim', 'Kiran', 'Klaas', 'Klaus',
        'Klemens', 'Kleopas', 'Knud', 'Knut', 'Kolja', 'Konrad', 'Konstantin',
        'Korbin', 'Korbinian', 'Kordt', 'Kristian', 'Kristof', 'Kristoffer',
        'Kuno', 'Kurt', 'Kyros', 'LLoyd', 'Lajos', 'Lambert', 'Lamberto',
        'Larry', 'Lars', 'Laslo', 'Lasse', 'Laurent', 'Laurente', 'Laurentius',
        'Laurenz', 'Laurenzo', 'Lawrence', 'Lazarus', 'Lazlo', 'Leander',
        'Lee', 'Leif', 'Leigh', 'Lennart', 'Lenny', 'Lenz', 'Leo', 'Leon',
        'Leonard', 'Leonardo', 'Leonce', 'Leone', 'Leonello', 'Leonhard',
        'Leopold', 'Leopoldo', 'Leroy', 'Lesley', 'Lester', 'Leverett', 'Levi',
        'Lew', 'Lewis', 'Lex', 'Liborius', 'Lienhard', 'Linus', 'Lion',
        'Lionel', 'Lobo', 'Loic', 'Lorenz', 'Lorenzo', 'Loris', 'Lothaire',
        'Lou', 'Louie', 'Louis', 'Lovis', 'Luc', 'Luca', 'Lucan', 'Lucas',
        'Luciano', 'Lucien', 'Lucius', 'Ludovico', 'Ludwig', 'Luigi', 'Luis',
        'Lukas', 'Luke', 'Lutger', 'Luther', 'Lutz', 'Lyonel', 'Maik', 'Malte',
        'Malwin', 'Manolito', 'Manolo', 'Manuel', 'Marc', 'Marcel', 'Marcello',
        'Marcellus', 'Marco', 'Marcus', 'Marek', 'Marian', 'Marin', 'Marino',
        'Marinus', 'Mario', 'Marius', 'Mark', 'Markus', 'Marlon', 'Maro',
        'Marten', 'Martin', 'Marvin', 'Massimo', 'Mathias', 'Mathieu',
        'Mathis', 'Matt', 'Matteo', 'Matthes', 'Matthew', 'Matthias',
        'Matthieu', 'Matthäus', 'Maurice', 'Mauritius', 'Mauritz', 'Maurizio',
        'Mauro', 'Maurus', 'Max', 'Maxence', 'Maxi', 'Maxime', 'Maximilian',
        'Maximilien', 'Melchior', 'Merlin', 'Michael', 'Michail', 'Michel',
        'Michele', 'Mick', 'Mickey', 'Miguel', 'Mika', 'Mikael', 'Mike',
        'Mikel', 'Miklos', 'Milan', 'Milo', 'Mirko', 'Miro', 'Miroslav',
        'Mischa', 'Mitja', 'Morgan', 'Moritz', 'Morris', 'Morten', 'Nat',
        'Nathan', 'Nathanael', 'Nathaniel', 'Nepomuk', 'Nero', 'Neron',
        'Newton', 'Niccolo', 'Nicholas', 'Nick', 'Nicki', 'Nico', 'Nicola',
        'Nicolai', 'Nicolaj', 'Nicolas', 'Niels', 'Nigel', 'Nikita', 'Niklas',
        'Niklaus', 'Niko', 'Nikodemus', 'Nikolai', 'Nikolaus', 'Nils', 'Noah',
        'Noel', 'Norbert', 'Norberto', 'Norman', 'Odin', 'Odo', 'Odysseus',
        'Olaf', 'Oleg', 'Oliver', 'Olivier', 'Oliviero', 'Olof', 'Oluf',
        'Omar', 'Omer', 'Orlando', 'Orson', 'Oskar', 'Osvaldo', 'Oswin',
        'Otello', 'Othello', 'Otto', 'Ove', 'Owain', 'Owen', 'Paco', 'Paddy',
        'Palmiro', 'Pancho', 'Paolo', 'Pascal', 'Pat', 'Patrice', 'Patricio',
        'Patricius', 'Patrick', 'Patrizio', 'Patrizius', 'Paul', 'Paulin',
        'Paulus', 'Pawel', 'Pedro', 'Peer', 'Pepe', 'Pepito', 'Peppone', 'Per',
        'Percy', 'Perez', 'Pete', 'Peter', 'Phil', 'Philip', 'Philipp',
        'Philippe', 'Philo', 'Piedro', 'Pier', 'Piero', 'Pierre', 'Piet',
        'Pieter', 'Pietro', 'Pinkus', 'Pippin', 'Pitt', 'Pius', 'Placide',
        'Placido', 'Placidus', 'Poldi', 'Quint', 'Quintin', 'Quintinus',
        'Quintus', 'Quirin', 'Quirino', 'Raffaele', 'Raffaello', 'Raffaelo',
        'Raimondo', 'Raimund', 'Raimundo', 'Rainer', 'Rainier', 'Ralf',
        'Ralph', 'Ramon', 'Randolf', 'Randolph', 'Randy', 'Raoul', 'Raphael',
        'Rasmus', 'Rasul', 'Raul', 'Ray', 'Raymond', 'Regnier', 'Reik',
        'Reiner', 'Remo', 'Renato', 'Renatus', 'Renaud', 'Rene', 'Renja',
        'Reto', 'Reynold', 'Ricardo', 'Riccardo', 'Rick', 'Ricky', 'Rico',
        'Rinaldo', 'Robby', 'Robert', 'Roberto', 'Robin', 'Rocco', 'Rock',
        'Rocky', 'Rod', 'Rodolfo', 'Rodolphe', 'Rodrigo', 'Rodrigue',
        'Rodrique', 'Roger', 'Roland', 'Rolando', 'Rolf', 'Romain', 'Roman',
        'Romano', 'Romeo', 'Romero', 'Ronald', 'Ronan', 'Ronny', 'Rory',
        'Ross', 'Rowan', 'Rowland', 'Roy', 'Ruben', 'Rudolf', 'Rudolph',
        'Ruggero', 'Rupert', 'Ryan', 'Salomon', 'Salomone', 'Salvador',
        'Salvator', 'Salvatore', 'Sam', 'Sammy', 'Samuel', 'Samuele', 'Sander',
        'Sandor', 'Sandro', 'Sandy', 'Sascha', 'Sauveur', 'Schorsch', 'Scipio',
        'Scott', 'Sean', 'Sebastian', 'Sebastiano', 'Sebastien', 'Selim',
        'Semjon', 'Sepp', 'Serenus', 'Serge', 'Sergej', 'Sergio', 'Sergius',
        'Servatius', 'Severiano', 'Severin', 'Severo', 'Sidney', 'Sidonius',
        'Silas', 'Silvain', 'Silvan', 'Silvano', 'Silvanus', 'Silverio',
        'Silverius', 'Silvester', 'Silvestro', 'Silvio', 'Silvius', 'Simjon',
        'Simon', 'Simone', 'Sinclair', 'Sixt', 'Sixtus', 'Slade', 'Solomon',
        'Spencer', 'Stan', 'Stanislaus', 'Stanislaw', 'Stanley', 'Stefan',
        'Stefano', 'Steffen', 'Sten', 'Stephan', 'Stephen', 'Steve', 'Steven',
        'Stewart', 'Stig', 'Stuart', 'Sven', 'Sylvain', 'Sylvester', 'Söncke',
        'Sören', 'Tam', 'Tarek', 'Tassilo', 'Tasso', 'Ted', 'Teddy',
        'Teobaldo', 'Thaddäus', 'Theo', 'Theodor', 'Theodore', 'Thierry',
        'Thimotheus', 'Thomas', 'Thommy', 'Thoralf', 'Thorben', 'Thore',
        'Thorsten', 'Tiberio', 'Tiberius', 'Tibor', 'Till', 'Tim', 'Timmy',
        'Timo', 'Timofej', 'Timon', 'Timoteo', 'Timothee', 'Timotheus',
        'Timothy', 'Tin', 'Tito', 'Titus', 'Tizian', 'Tiziano', 'Tjade',
        'Tjark', 'Tobi', 'Tobia', 'Tobiah', 'Tobias', 'Tobie', 'Tobis', 'Toby',
        'Tom', 'Tommaso', 'Tommy', 'Toni', 'Tonio', 'Tony', 'Torben', 'Torin',
        'Torsten', 'Tristan', 'Tycho', 'Tyler', 'Tyson', 'Udo', 'Ugo',
        'Ugolino', 'Ulf', 'Uli', 'Ulli', 'Ulric', 'Ulrich', 'Ulrico',
        'Umberto', 'Urbain', 'Urban', 'Urbano', 'Urias', 'Uriel', 'Ursus',
        'Uwe', 'Valentiano', 'Valentin', 'Valentino', 'Valerian', 'Valerio',
        'Valerius', 'Valery', 'Vasco', 'Veit', 'Veltin', 'Vernon', 'Vicente',
        'Vico', 'Victor', 'Viktor', 'Vincent', 'Vincenzo', 'Vinzenez',
        'Vinzenz', 'Virgil', 'Vitalis', 'Vito', 'Vittore', 'Vittoriano',
        'Vittorio', 'Volker', 'Wallace', 'Walt', 'Warner', 'Warren', 'Wido',
        'Wigand', 'Wilbur', 'Willi', 'William', 'Wilpert', 'Winston', 'Wolf',
        'Wolfgang', 'Woodrow', 'Woody', 'Xaver',
    )

    first_names_female = (
        'Abby', 'Abelina', 'Abigail', 'Adelaide', 'Adeline', 'Adina',
        'Adriana', 'Adrienne', 'Afra', 'Agatha', 'Agnes', 'Aida', 'Aimee',
        'Aischa', 'Albertine', 'Alea', 'Aleksandra', 'Alena', 'Alessa',
        'Alessandra', 'Alessia', 'Alexa', 'Alexandra', 'Alexia', 'Alexis',
        'Alice', 'Alicia', 'Alida', 'Alina', 'Aline', 'Alisa', 'Alissa',
        'Alisson', 'Amabella', 'Amadea', 'Amanda', 'Amelia', 'Amelie', 'Amina',
        'Amy', 'Ana', 'Anastasia', 'Andrea', 'Andrina', 'Anette', 'Angela',
        'Angelika', 'Angelina', 'Angelique', 'Anina', 'Anine', 'Anita', 'Anja',
        'Anjalie', 'Anke', 'Ann', 'Anna', 'Annabel', 'Annabell', 'Annabella',
        'Annabelle', 'Anne', 'Annett', 'Annette', 'Annika', 'Annina', 'Antje',
        'Antoinette', 'Antonella', 'Antonia', 'Arabella', 'Ariadne', 'Ariana',
        'Ariane', 'Arianna', 'Ariella', 'Arielle', 'Arlene', 'Arlette',
        'Arwenna', 'Ashley', 'Asta', 'Astrid', 'Audrey', 'Aurelia', 'Barbara',
        'Bastiane', 'Bea', 'Beata', 'Beatrice', 'Beatrix', 'Becky', 'Belinda',
        'Bella', 'Bellana', 'Belle', 'Benedikta', 'Benita', 'Bente', 'Beppina',
        'Berenike', 'Berit', 'Bernadett', 'Bernadette', 'Bernadine', 'Betina',
        'Betsy', 'Bettina', 'Betty', 'Bianca', 'Bianka', 'Bibiana', 'Bibiane',
        'Birgit', 'Birgitt', 'Bodil', 'Bridget', 'Brigitta', 'Brigitte',
        'Britta', 'Bärbel', 'Caitlin', 'Cameron', 'Camilla', 'Camille',
        'Cammy', 'Cara', 'Carin', 'Carina', 'Carinna', 'Carla', 'Carmela',
        'Carmelia', 'Carmen', 'Carol', 'Carola', 'Carole', 'Carolin',
        'Carolina', 'Caroline', 'Carolyn', 'Carolyne', 'Cassandra', 'Cassie',
        'Catalin', 'Caterina', 'Catharina', 'Catherine', 'Cathrin', 'Cathrine',
        'Cathy', 'Catina', 'Catrin', 'Catriona', 'Cecile', 'Cecilia',
        'Cecilie', 'Celeste', 'Celestine', 'Celina', 'Celine', 'Chantal',
        'Charleen', 'Charlotte', 'Chatrina', 'Chelsea', 'Chiara', 'Chloe',
        'Chrissy', 'Christa', 'Christiana', 'Christiane', 'Christin',
        'Christina', 'Christine', 'Chyna', 'Ciara', 'Cinderella', 'Cindy',
        'Cinja', 'Cira', 'Claire', 'Clara', 'Clarissa', 'Claudette', 'Claudia',
        'Claudine', 'Clea', 'Cleannis', 'Clementia', 'Clementine', 'Cleo',
        'Clio', 'Cliona', 'Clodia', 'Cloris', 'Coletta', 'Colette', 'Connie',
        'Conny', 'Constance', 'Constanze', 'Cora', 'Coral', 'Coralie',
        'Cordelia', 'Cordula', 'Corin', 'Corina', 'Corinna', 'Corinne',
        'Cornelia', 'Cosette', 'Cosima', 'Cynthia', 'Daisy', 'Dajana',
        'Daliah', 'Damaris', 'Damia', 'Damiana', 'Dana', 'Dania', 'Danica',
        'Daniela', 'Daniele', 'Daniella', 'Danielle', 'Danja', 'Daphne',
        'Darcie', 'Daria', 'Darina', 'Dawn', 'Dayna', 'Debbie', 'Debby',
        'Debora', 'Deborah', 'Deetya', 'Delia', 'Delphine', 'Dena', 'Denise',
        'Desdemona', 'Desideria', 'Desiree', 'Diana', 'Diane', 'Didina',
        'Dina', 'Dinah', 'Dolly', 'Dolores', 'Domenica', 'Dominika',
        'Dominique', 'Donna', 'Dora', 'Doreen', 'Dorina', 'Doris', 'Dorit',
        'Doro', 'Dorothea', 'Dorothee', 'Dorothy', 'Dunja', 'Ebony', 'Edda',
        'Edita', 'Edvige', 'Edwina', 'Eike', 'Eila', 'Eileen', 'Ela', 'Elaine',
        'Eleanor', 'Elektra', 'Elena', 'Eleonora', 'Eleonore', 'Eliane',
        'Elisa', 'Elisabeth', 'Elise', 'Elizabeth', 'Elke', 'Ella', 'Ellen',
        'Elly', 'Eloise', 'Elsa', 'Elsbeth', 'Elvira', 'Elvire', 'Emanuela',
        'Emanuelle', 'Emilia', 'Emilie', 'Emily', 'Emma', 'Enrica', 'Enya',
        'Erika', 'Erin', 'Ernesta', 'Ernestina', 'Ernestine', 'Esmerelda',
        'Esra', 'Estella', 'Estelle', 'Ester', 'Esther', 'Etiennette',
        'Eudoxia', 'Eugenia', 'Eunike', 'Euphemia', 'Euphrasia', 'Eusebia',
        'Eva', 'Evangelina', 'Evania', 'Eve', 'Evelien', 'Evelin', 'Eveline',
        'Evelyn', 'Evelyne', 'Evette', 'Evi', 'Evita', 'Fabiane', 'Fabienne',
        'Fabiola', 'Faith', 'Fanny', 'Farrah', 'Fatima', 'Faustina',
        'Faustine', 'Fay', 'Faye', 'Faylinn', 'Federica', 'Fedora', 'Fee',
        'Feli', 'Felice', 'Felicia', 'Felicitas', 'Felicity', 'Felizitas',
        'Feodora', 'Fergie', 'Fidelia', 'Filia', 'Filiz', 'Finetta', 'Finja',
        'Fiona', 'Fjodora', 'Flavia', 'Fleur', 'Fleur', 'Flo', 'Flora',
        'Florence', 'Florentina', 'Florentine', 'Floria', 'Floriane',
        'Florida', 'Florinda', 'Floris', 'Fortuna', 'Frances', 'Francesca',
        'Francisca', 'Franka', 'Franzi', 'Franziska', 'Frauke', 'Freya',
        'Friederike', 'Gabriela', 'Gabriele', 'Gabriella', 'Gabrielle', 'Gaby',
        'Gail', 'Galatea', 'Galina', 'Gazelle', 'Gela', 'Geneva', 'Genoveva',
        'Georgette', 'Georgia', 'Georgina', 'Geraldene', 'Geraldine',
        'Germain', 'Germaine', 'Germana', 'Ghita', 'Gianna', 'Gigi', 'Gill',
        'Gillian', 'Gina', 'Ginevra', 'Ginger', 'Ginny', 'Giovanna', 'Gisela',
        'Gisele', 'Gisella', 'Giselle', 'Gitta', 'Giulia', 'Giuliana',
        'Giulietta', 'Giuseppa', 'Giuseppina', 'Giustina', 'Gladys', 'Gloria',
        'Glory', 'Goldie', 'Goldy', 'Grace', 'Gratia', 'Gratiana', 'Grazia',
        'Greta', 'Gretel', 'Gunda', 'Gwen', 'Gwenda', 'Gwendolin', 'Gwendolyn',
        'Gypsy', 'Hannah', 'Hanne', 'Harmony', 'Harriet', 'Hazel', 'Hedi',
        'Hedy', 'Heide', 'Heidi', 'Heike', 'Helen', 'Helena', 'Helene',
        'Helin', 'Hella', 'Hemma', 'Henrietta', 'Henriette', 'Henrike', 'Hera',
        'Hetty', 'Hilary', 'Hilda', 'Hilde', 'Holiday', 'Holli', 'Holly',
        'Hope', 'Ilana', 'Ilaria', 'Iliana', 'Iljana', 'Ilka', 'Ilona', 'Ilse',
        'Ilyssa', 'Imke', 'Ina', 'India', 'Indira', 'Indra', 'Ines', 'Inga',
        'Inge', 'Ingrid', 'Inka', 'Inken', 'Innozentia', 'Iona', 'Ira',
        'Irena', 'Irene', 'Irina', 'Iris', 'Irisa', 'Irma', 'Isabel',
        'Isabell', 'Isabella', 'Isabelle', 'Isis', 'Iva', 'Ivana', 'Ivona',
        'Ivonne', 'Jaclyn', 'Jacqueline', 'Jacqui', 'Jael', 'Jamari', 'Jan',
        'Jana', 'Jane', 'Janet', 'Janette', 'Janin', 'Janina', 'Janine',
        'Janique', 'Janna', 'Jannine', 'Jarla', 'Jasmin', 'Jasmina', 'Jasmine',
        'Jeanette', 'Jeanine', 'Jeanne', 'Jeannette', 'Jeannine', 'Jekaterina',
        'Jelena', 'Jenifer', 'Jenna', 'Jennelle', 'Jennessa', 'Jennie',
        'Jennifer', 'Jenny', 'Jennyfer', 'Jess', 'Jessica', 'Jessie',
        'Jessika', 'Jill', 'Joan', 'Joana', 'Joann', 'Joanna', 'Joelle',
        'Johanna', 'Jolanda', 'Jona', 'Jordana', 'Josee', 'Josefa', 'Josefina',
        'Josefine', 'Josepha', 'Josephine', 'Josiane', 'Josie', 'Jovita',
        'Joy', 'Joyce', 'Juana', 'Juanita', 'Judith', 'Judy', 'Julia',
        'Juliana', 'Juliane', 'Julianne', 'Julie', 'Juliet', 'Juliette',
        'July', 'June', 'Justina', 'Justine', 'Justise', 'Jutta', 'Jördis',
        'Kamilia', 'Kamilla', 'Karen', 'Karima', 'Karin', 'Karina', 'Karla',
        'Karola', 'Karolin', 'Karolina', 'Karoline', 'Kassandra', 'Katalin',
        'Katarina', 'Kate', 'Katharina', 'Katharine', 'Katherina', 'Katherine',
        'Kathleen', 'Kathrin', 'Kathrina', 'Kathryn', 'Kathy', 'Katinka',
        'Katja', 'Katjana', 'Katrin', 'Katrina', 'Katrine', 'Kayla', 'Keala',
        'Keelin', 'Kendra', 'Kerstin', 'Kiana', 'Kiara', 'Kim', 'Kira',
        'Kirsten', 'Kirstin', 'Kita', 'Klara', 'Klarissa', 'Klaudia',
        'Kleopatra', 'Kolina', 'Konstanze', 'Kora', 'Kordula', 'Kori',
        'Kornelia', 'Krista', 'Kristiane', 'Kristin', 'Kristina', 'Kristine',
        'Kyra', 'Käthe', 'Laila', 'Lana', 'Lara', 'Laria', 'Larissa', 'Laurel',
        'Lauren', 'Laurence', 'Laurentia', 'Lauretta', 'Lavina', 'Laya', 'Lea',
        'Leah', 'Leandra', 'Lee', 'Leigh', 'Leila', 'Lena', 'Leona', 'Leonie',
        'Leontine', 'Leopoldine', 'Lesley', 'Leslie', 'Levana', 'Levia', 'Lia',
        'Liane', 'Libusa', 'Licia', 'Lidia', 'Liesa', 'Liesbeth', 'Liese',
        'Liesel', 'Lilian', 'Liliane', 'Lilith', 'Lilli', 'Lillian', 'Lilo',
        'Lily', 'Lina', 'Linda', 'Lioba', 'Lisa', 'Lisbeth', 'Lise', 'Lisette',
        'Liv', 'Livana', 'Livia', 'Liz', 'Liza', 'Lizzie', 'Lola', 'Lora',
        'Lorena', 'Loretta', 'Lori', 'Lorraine', 'Lotte', 'Lotus', 'Louise',
        'Luana', 'Luca', 'Lucia', 'Luciana', 'Lucie', 'Lucy', 'Luigia',
        'Luisa', 'Luise', 'Luna', 'Luzia', 'Lydia', 'Lydie', 'Lynette', 'Lynn',
        'Lätizia', 'Maddalena', 'Madelaine', 'Madeleine', 'Madeline',
        'Madison', 'Madita', 'Madleine', 'Madlen', 'Madlene', 'Mae', 'Magda',
        'Magdalena', 'Maggy', 'Magret', 'Maia', 'Maike', 'Maiken', 'Mailin',
        'Maja', 'Malea', 'Malee', 'Malin', 'Malina', 'Mandy', 'Manja', 'Manon',
        'Manuela', 'Mara', 'Maraike', 'Marcella', 'Marcelle', 'Marcia',
        'Mareike', 'Maren', 'Margaret', 'Margareta', 'Margarete', 'Margaretha',
        'Margarita', 'Margaritha', 'Margherita', 'Margit', 'Margitta',
        'Margot', 'Margret', 'Margreth', 'Marguerite', 'Maria', 'Mariam',
        'Marian', 'Mariana', 'Marianna', 'Marianne', 'Marie', 'Marieke',
        'Mariella', 'Marielle', 'Marietta', 'Marija', 'Marika', 'Marilies',
        'Marilyn', 'Marina', 'Marion', 'Marisa', 'Marissa', 'Marita',
        'Maritta', 'Marjorie', 'Marla', 'Marleen', 'Marlen', 'Marlena',
        'Marlene', 'Marlies', 'Marlis', 'Marsha', 'Martha', 'Marthe',
        'Martina', 'Mary', 'Maryse', 'Mascha', 'Mathilda', 'Mathilde',
        'Matilde', 'Mattea', 'Maude', 'Maura', 'Maureen', 'Maximiliane', 'May',
        'Maya', 'Meg', 'Megan', 'Meike', 'Melanie', 'Melia', 'Melina',
        'Melinda', 'Melissa', 'Melitta', 'Melodie', 'Meloney', 'Mercedes',
        'Meret', 'Meri', 'Merle', 'Merline', 'Meryem', 'Mia', 'Micaela',
        'Michaela', 'Michele', 'Michelle', 'Milena', 'Milla', 'Milva', 'Mimi',
        'Minerva', 'Minna', 'Mira', 'Mirabella', 'Mireille', 'Mirella',
        'Mireya', 'Miriam', 'Mirijam', 'Mirjam', 'Moesha', 'Moira', 'Mona',
        'Moni', 'Monica', 'Monika', 'Monique', 'Monja', 'Morgane', 'Muriel',
        'Myriam', 'Nadin', 'Nadine', 'Nadja', 'Nadjana', 'Naemi', 'Nancy',
        'Nanette', 'Nani', 'Naomi', 'Nastasja', 'Natalia', 'Natalie',
        'Natanja', 'Natascha', 'Nathalie', 'Neeja', 'Nena', 'Neria', 'Nerine',
        'Nicol', 'Nicola', 'Nicole', 'Nicoletta', 'Nicolette', 'Nike',
        'Nikola', 'Nina', 'Ninja', 'Ninon', 'Noa', 'Noelle', 'Noemi', 'Noemie',
        'Nora', 'Norma', 'Nuala', 'Olga', 'Olivia', 'Ophelia', 'Orania',
        'Orla', 'Ornella', 'Orsola', 'Ottilie', 'Paloma', 'Pam', 'Pamela',
        'Pandora', 'Paola', 'Paolina', 'Pascale', 'Pat', 'Patrice', 'Patricia',
        'Patrizia', 'Patsy', 'Patty', 'Paula', 'Paulette', 'Paulina',
        'Pauline', 'Penelope', 'Pepita', 'Petra', 'Philine', 'Philippa',
        'Philomele', 'Philomena', 'Phoebe', 'Phyllis', 'Pia', 'Pier', 'Prica',
        'Prisca', 'Priscilla', 'Priscille', 'Priska', 'Rachel', 'Rachel',
        'Rachelle', 'Radomila', 'Rafaela', 'Raffaela', 'Raffaella', 'Ragna',
        'Rahel', 'Raja', 'Ramona', 'Raphaela', 'Raquel', 'Rebecca', 'Rebekka',
        'Regina', 'Regine', 'Reisha', 'Renata', 'Renate', 'Renee', 'Resi',
        'Rhea', 'Rhoda', 'Rhonda', 'Ricarda', 'Riccarda', 'Rike', 'Rita',
        'Roberta', 'Romana', 'Romina', 'Romy', 'Ronja', 'Rosa', 'Rosalia',
        'Rosalie', 'Rosalinda', 'Rosalinde', 'Rosaline', 'Rose', 'Roseline',
        'Rosetta', 'Rosette', 'Rosi', 'Rosina', 'Rosine', 'Rossana',
        'Roswitha', 'Roxana', 'Roxane', 'Roxanne', 'Roxy', 'Rubina', 'Ruth',
        'Sabine', 'Sabrina', 'Sahra', 'Sally', 'Salome', 'Salvina', 'Samanta',
        'Samantha', 'Samira', 'Sandra', 'Sandrina', 'Sandrine', 'Sandy',
        'Sanne', 'Sanya', 'Saphira', 'Sara', 'Sarah', 'Sarina', 'Sascha',
        'Saskia', 'Scarlet', 'Scarlett', 'Schirin', 'Selina', 'Selma',
        'Serafina', 'Seraina', 'Seraphin', 'Seraphina', 'Seraphine', 'Serena',
        'Severina', 'Severine', 'Shana', 'Shanaya', 'Shantala', 'Shari',
        'Sharlene', 'Sharon', 'Sheena', 'Sheila', 'Sheryl', 'Shirin',
        'Shirley', 'Shirlyn', 'Sibilla', 'Sibyl', 'Sibylle', 'Siegrid',
        'Sigrid', 'Sigrun', 'Silja', 'Silke', 'Silvana', 'Silvia', 'Silviane',
        'Simona', 'Simone', 'Simonette', 'Simonne', 'Sina', 'Sindy', 'Sinja',
        'Sissy', 'Skyla', 'Smarula', 'Smilla', 'Sofia', 'Sofie', 'Sonia',
        'Sonja', 'Sonnele', 'Sonya', 'Sophia', 'Sophie', 'Soraya', 'Stefanie',
        'Steffi', 'Stella', 'Stephanie', 'Sumehra', 'Summer', 'Susan',
        'Susanna', 'Susanne', 'Susi', 'Suzan', 'Suzanne', 'Suzette', 'Svea',
        'Svenja', 'Swane', 'Sybilla', 'Sybille', 'Sydney', 'Sylvana', 'Sylvia',
        'Sylvie', 'Tabitha', 'Taissa', 'Tamara', 'Tamina', 'Tania', 'Tanita',
        'Tanja', 'Tara', 'Tatiana', 'Tatjana', 'Taya', 'Tecla', 'Telka',
        'Teodora', 'Teona', 'Teresa', 'Terry', 'Tess', 'Tessa', 'Tessie',
        'Thea', 'Thekla', 'Theodora', 'Theres', 'Theresa', 'Therese',
        'Theresia', 'Tiana', 'Tiffany', 'Tilly', 'Timna', 'Tina', 'Tiziana',
        'Tonja', 'Toril', 'Tosca', 'Tracey', 'Traudl', 'Trixi', 'Tycho',
        'Tyra', 'Ulla', 'Ulli', 'Ulrica', 'Ulrike', 'Undine', 'Urania',
        'Ursel', 'Ursina', 'Ursula', 'Ursule', 'Uschi', 'Uta', 'Ute',
        'Valentina', 'Valentine', 'Valeria', 'Valerie', 'Valeska', 'Vanadis',
        'Vanessa', 'Vanja', 'Varinka', 'Venetia', 'Vera', 'Verena', 'Verona',
        'Veronica', 'Veronika', 'Veronique', 'Vesla', 'Vicky', 'Victoire',
        'Victoria', 'Viki', 'Viktoria', 'Vilja', 'Viola', 'Violet', 'Violetta',
        'Violette', 'Virginia', 'Virginie', 'Vittoria', 'Viviana', 'Viviane',
        'Vivien', 'Vivienne', 'Vreneli', 'Vreni', 'Vroni', 'Wencke', 'Weneke',
        'Wibke', 'Wilja', 'Willow', 'Wilma',
    )

    first_names = first_names_male + first_names_female

    last_names = (
        'Ackermann', 'Adler', 'Adolph', 'Albers', 'Anders', 'Atzler', 'Aumann',
        'Austermühle', 'Bachmann', 'Barkholz', 'Barth', 'Bauer', 'Baum',
        'Becker', 'Beckmann', 'Beer', 'Beier', 'Bender', 'Benthin', 'Berger',
        'Beyer', 'Bien', 'Biggen', 'Binner', 'Birnbaum', 'Bloch', 'Blümel',
        'Bohlander', 'Bohnbach', 'Bolander', 'Bolnbach', 'Bolzmann', 'Bonbach',
        'Boucsein', 'Briemer', 'Bruder', 'Buchholz', 'Budig', 'Butte', 'Bähr',
        'Bärer', 'Börner', 'Carsten', 'Caspar', 'Christoph', 'Cichorius',
        'Conradi', 'Davids', 'Dehmel', 'Dickhard', 'Dietz', 'Dippel',
        'Ditschlerin', 'Dobes', 'Dowerg', 'Drewes', 'Drub', 'Drubin', 'Dussen',
        'Dussen van', 'Döhn', 'Döring', 'Dörr', 'Dörschner', 'Eberhardt',
        'Ebert', 'Eberth', 'Eckbauer', 'Ehlert', 'Eigenwillig', 'Eimer',
        'Ernst', 'Etzler', 'Etzold', 'Faust', 'Fechner', 'Fiebig', 'Finke',
        'Fischer', 'Flantz', 'Fliegner', 'Franke', 'Freudenberger', 'Fritsch',
        'Fröhlich', 'Förster', 'Gehringer', 'Geisel', 'Geisler', 'Geißler',
        'Gerlach', 'Gertz', 'Gierschner', 'Gieß', 'Girschner', 'Gnatz',
        'Gorlitz', 'Gotthard', 'Graf', 'Grein Groth', 'Gröttner', 'Gude',
        'Gumprich', 'Gunpf', 'Gute', 'Gutknecht', 'Haase', 'Haering', 'Hahn',
        'Hamann', 'Hande', 'Harloff', 'Hartmann', 'Hartung', 'Hauffer',
        'Hecker', 'Heidrich', 'Hein', 'Heinrich', 'Heintze', 'Heinz',
        'Hellwig', 'Henck', 'Hendriks', 'Henk', 'Henschel', 'Hentschel',
        'Hering', 'Hermann', 'Hermighausen', 'Herrmann', 'Hertrampf', 'Heser',
        'Hesse', 'Hethur', 'Hettner', 'Heuser', 'Heydrich', 'Heß', 'Hiller',
        'Hoffmann', 'Hofmann', 'Holsten', 'Holt', 'Holzapfel', 'Hornich',
        'Hornig', 'Huhn', 'Hänel', 'Häring', 'Höfig', 'Hölzenbecher', 'Hörle',
        'Hövel', 'Hübel', 'Jacob', 'Jacobi', 'Jessel', 'Jockel', 'Johann',
        'Jopich', 'Junck', 'Juncken', 'Jungfer', 'Junitz', 'Junk', 'Junken',
        'Jäckel', 'Jähn', 'Jäkel', 'Jäntsch', 'Jüttner', 'Kabus', 'Kade',
        'Kallert', 'Kambs', 'Karge', 'Karz', 'Kaul', 'Kensy', 'Keudel',
        'Killer', 'Kitzmann', 'Klapp', 'Klemm', 'Klemt', 'Klingelhöfer',
        'Klotz', 'Knappe', 'Kobelt', 'Koch', 'Koch II', 'Kohl', 'Kostolzin',
        'Kramer', 'Kranz', 'Krause', 'Kraushaar', 'Krebs', 'Krein', 'Kreusel',
        'Kroker', 'Kruschwitz', 'Kuhl', 'Kusch', 'Käster', 'Köhler', 'Köster',
        'Kühnert', 'Lachmann', 'Ladeck', 'Lange', 'Langern', 'Lehmann',
        'Liebelt', 'Lindau', 'Lindner', 'Linke', 'Loos', 'Lorch', 'Losekann',
        'Löchel', 'Löffler', 'Löwer', 'Lübs', 'Mangold', 'Mans', 'Margraf',
        'Martin', 'Matthäi', 'Meister', 'Mende', 'Mentzel', 'Metz', 'Meyer',
        'Mielcarek', 'Mies', 'Misicher', 'Mitschke', 'Mohaupt', 'Mosemann',
        'Mude', 'Mälzer', 'Möchlichen', 'Mühle', 'Mülichen', 'Müller', 'Naser',
        'Nerger', 'Nette', 'Neureuther', 'Neuschäfer', 'Niemeier', 'Noack',
        'Nohlmans', 'Oderwald', 'Oestrovsky', 'Ortmann', 'Otto', 'Paffrath',
        'Patberg', 'Pechel', 'Pergande', 'Peukert', 'Pieper', 'Plath', 'Pohl',
        'Preiß', 'Pruschke', 'Putz', 'Pärtzelt', 'Pölitz', 'Radisch',
        'Reichmann', 'Reinhardt', 'Reising', 'Renner', 'Reuter', 'Riehl',
        'Ring', 'Ritter', 'Rogge', 'Rogner', 'Rohleder', 'Roht', 'Rose',
        'Rosemann', 'Rosenow', 'Roskoth', 'Rudolph', 'Ruppersberger',
        'Ruppert', 'Rust', 'Rädel', 'Röhrdanz', 'Röhricht', 'Römer',
        'Rörricht', 'Sager', 'Salz', 'Sauer', 'Schaaf', 'Schacht', 'Scheel',
        'Scheibe', 'Schenk', 'Scheuermann', 'Schinke', 'Schleich', 'Schleich',
        'Schlosser', 'Schmidt', 'Schmidtke', 'Schmiedecke', 'Schmiedt',
        'Scholl', 'Scholtz', 'Scholz', 'Schomber', 'Schottin', 'Schuchhardt',
        'Schulz', 'Schuster', 'Schweitzer', 'Schwital', 'Schäfer', 'Schönland',
        'Schüler', 'Segebahn', 'Seidel', 'Seifert', 'Seifert', 'Seip',
        'Siering', 'Sontag', 'Sorgatz', 'Speer', 'Spieß', 'Stadelmann',
        'Stahr', 'Staude', 'Steckel', 'Steinberg', 'Stey', 'Stiebitz',
        'Stiffel', 'Stoll', 'Stolze', 'Striebitz', 'Stroh', 'Stumpf', 'Sucker',
        'Säuberlich', 'Söding', 'Sölzer', 'Süßebier', 'Textor', 'Thanel',
        'Thies', 'Tintzmann', 'Tlustek', 'Trapp', 'Trommler', 'Trub', 'Trubin',
        'Trupp', 'Tröst', 'Trüb', 'Tschentscher', 'Täsche', 'Ullmann',
        'Ullrich', 'Vogt', 'Vollbrecht', 'Wagenknecht', 'Wagner', 'Walter',
        'Warmer', 'Weihmann', 'Weimer', 'Weinhage', 'Weinhold', 'Weitzel',
        'Weiß', 'Weller', 'Wende', 'Wernecke', 'Werner', 'Wesack', 'Wiek',
        'Wieloch', 'Wilms', 'Wilmsen', 'Winkler', 'Wirth', 'Wohlgemut', 'Wulf',
        'Wulff', 'Wähner', 'Zahn', 'Ziegert', 'Zimmer', 'Zirme', 'Zobel',
        'Zorbach', 'Zänker', 'auch Schlauchin',
    )

    prefixes_male = (
        'Herr', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )
    prefixes_female = (
        'Frau', 'Dr.', 'Ing.', 'Dipl.-Ing.', 'Prof.', 'Univ.Prof.',
    )

    suffixes = ('B.Sc.', 'B.A.', 'B.Eng.', 'MBA.', )