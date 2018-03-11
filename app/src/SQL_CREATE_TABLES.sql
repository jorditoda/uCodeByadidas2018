CREATE TABLE Users (
    username varchar(255),
    age int,
    gender tinyint,
    height smallint,
    postal_code int,
    expenses float,
    PRIMARY KEY(username)
);

CREATE TABLE Products (
    idProduct int,
    urlPhoto varchar(255),
    price float,
    PRIMARY KEY(idProduct)
);

CREATE TABLE Interests (
    idInterest int,
    nameOfInterest varchar(255),
    PRIMARY KEY(idInterest)
);
CREATE TABLE Experiences (
    idExperience int,
    expDescription varchar(255),
    PRIMARY KEY(idExperience)
);

CREATE TABLE RelInterestUser (
    idInterest int,
    username varchar(255),

    CONSTRAINT idRelationIntUs PRIMARY KEY(idInterest, username),
    CONSTRAINT RelIntUser FOREIGN KEY (username) REFERENCES Users(username),
    CONSTRAINT idInterestInt FOREIGN KEY (idInterest) REFERENCES Interests(idInterest)
);

CREATE TABLE AdquiredProducts (
    idProduct int,
    username varchar(255),

    CONSTRAINT idAdquiredProducts PRIMARY KEY(idProduct, username),
    CONSTRAINT idProductAdPr FOREIGN KEY(idProduct) REFERENCES Products(idProduct),
    CONSTRAINT usernameAdPr FOREIGN KEY(username) REFERENCES Users(username)

);

CREATE TABLE ExperiencesHistory (
    idExperience int,
    username varchar(255),
    dateOfShow DATE,
    CONSTRAINT idExpHistory PRIMARY KEY(idExperience, username),
    CONSTRAINT expHistoryIdExp FOREIGN KEY(idExperience) REFERENCES Experiences(idExperience),
    CONSTRAINT expHistUsername FOREIGN KEY(username) REFERENCES Users(username)

);
