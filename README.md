#### Flatiron_School_Final

## Goal:
A study of Starcraft 2 replay data in an attempt to identify strategy exterior to expert knowledge

## Web Scrape:
While the Starcraft 2 replay files are not found in this repository, The means by which one can retrieve them are. In these scripts, I use *BeautifulSoup*, *selenium* and *requests* among many other libraries to pull replays from https://gggreplays.com/ and https://lotv.spawningtool.com/. Using Crontab -e, I am able to continuously scrape from these sites and populate psql database. 

In total ~> 120,000 replay files spanning 5 years and 7 leagues, among many other metrics, were collected. For the purposes of this project A subset of replays, particularly those belonging to professional players, were used due not only for the time constraint, but due to the diverse range of player strategy displayed at that level.

## Extract Transform Load:
Using the Flask-SQLAlchemy python framework a cyclic model of replay elements was constructed:

1. (Users) have many (Participants)
2. (Participants) have many (Events) have one (Game, User)
3. (Games) have many (Participants)
4. (Events) have one (Participant)

This intermediary object (Participant) works to simplify queries and relationships between (Games, Users, Events) and hosts a series of additional variable information from the previous Players class.

With the subset of replays committed to a SQLlite3 database, the raw information was then transformed into a sequential aggregate form.

*ie.*
(game, participant, sequence, train_Marine, train_Marauder, build_Barracks, ...)
1. a_1 = (100, 4, 0, 0, 0, 0, 0, ...)
2. a_2 = (100, 4, 1, 0, 1, 0, 0, ...)
3. a_3 = (100, 4, 2, 1, 0, 0, 0, ...)
4. a_4 = (100, 4, 3, 0, 1, 0, 0, ...)

*into*
(game, participant, action, train_Marine, train_Marauder, build_Barracks, ...)
1. a_1 = (100, 4, 0, 0, 0, 0, 0, ...)
2. a_2 = (100, 4, 1, 0, 1, 0, 0, ...)
3. a_3 = (100, 4, 2, 1, 1, 0, 0, ...)
4. a_4 = (100, 4, 3, 1, 2, 0, 0, ...)

![Image of data](http://oi68.tinypic.com/2wfl0fd.jpg)
_figure above displays all Terran professional games (buildings constructed) notice the clear directionality of the tendrils._

to reflect the current state of the game for one of the two participants. Notice, with (game, participant, action) removed, the bulk can be considered a one dimensional curve in Rn whose rate with respect to order of action belongs to the hypercube Rn and |a_(n)| < |a_(n+m)| for all n and m belong to the Naturals.

## Regression - Singular Vector
For each games sequence of events, I preformed a Principal Component Analysis reduction of dimensionally -> R1 as a means to extract the first singular vector. This, by the definition of the first singular vector [link_to_paper](https://www.cs.cmu.edu/~venkatg/teaching/CStheory-infoage/book-chapter-4.pdf) (Section 1.1), vector is a regressive representation of the direction of the propagation of events of each game. This was chosen as a representation not only for its speed and interpretability, but for its ability to capture the events for each game in its totality in a single vector. There are certainly disadvantages to this approach with a loss of information (High Bias) and lack of invertibility, but it suited the project goal well enough. Additionally, a hypersphere suite is constructed as a means to transform singular vectors into spherical coordinate system for ease of use in clustering algorithms. 

![Image of data](http://oi64.tinypic.com/34hjhuf.jpg)
_The figure above displays sigular vectors for Zerg professional games_

## Unsupervised K-Means - Euclidian:
Equipped with our singular vector representation for each game's events, I carried out unsupervised KMeans, with a Euclidian metric and GaussianMixture clustering on these singular vectors. With this algorithm, we were attempting to identify a collection of naturally occurring strategies in the game of Starcraft. I intend on trying several additional methods including a cosine similarity metric, which I believe will parse the singular vectors best according to an adjusted silhouette score metric.  

## Next Steps:
1. Gaussian Mixture and K-means on spherical coordinates
