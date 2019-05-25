"""File that contains the database creation script"""
import mysql.connector

#Quote list
QUOTES = (("Dans la vie on ne fait pas ce que l'on veut mais on est \
            responsable de ce que l'on est.", "Jean-Paul Sartre", "Vie"),
          ("La vie est un mystère qu'il faut vivre, et non un problème à \
            résoudre.", "Gandhi", "Vie"),
          ("La vie, c'est comme une bicyclette, il faut avancer pour ne pas \
            perdre l'équilibre.", "Albert Einstein", "Vie"),
          ("Pour critiquer les gens il faut les connaître, et pour les \
            connaître, il faut les aimer.", "Coluche", "Gens"),
          ("La règle d'or de la conduite est la tolérance mutuelle, car \
            nous ne penserons jamais tous de la même façon, nous ne verrons \
            qu'une partie de la vérité et sous des angles différents.", \
            "Gandhi", "Gens"),
          ("Choisissez un travail que vous aimez et vous n'aurez pas à \
            travailler un seul jour de votre vie.", "Confucius", "Travail"),
          ("Exige beaucoup de toi-même et attends peu des autres. Ainsi \
            beaucoup d'ennuis te seront épargnés.", "Confucius", "Gens"),
          ("Trois sortes d'amis sont utiles, trois sortes d'amis sont \
            néfastes. Les utiles : un ami droit, un ami fidèle, un ami \
            cultivé. Les néfastes : un ami faux, un ami mou, un ami bavard.", \
            "Confucius", "Amitié"),
          ("Si tu rencontres un homme de valeur, cherche à lui ressembler. \
            Si tu rencontres un homme médiocre, cherche ses défauts en \
            toi-même.", "Confucius", "Gens"),
          ("Quand on ne sait pas ce qu'est la vie, comment pourrait-on \
            savoir ce qu'est la mort ?", "Confucius", "Vie"),
          ("Celui qui ne progresse pas chaque jour, recule chaque jour.", \
            "Confucius", "Vie"),
          ("Ecoutez beaucoup, afin de diminuer vos doutes ; \
            soyez attentifs à ce que vous dites, afin de ne rien dire de \
            superflu ; alors, vous commettrez rarement des fautes.", \
            "Confucius", "Autre"),
          ("La haine tue toujours, l'amour ne meurt jamais.", "Gandhi", \
            "Amour"),
          ("Un seul être vous manque et tout est dépeuplé.", \
            "Lamartine", "Amour"),
          ("Le sentiment de ne pas être aimé est la plus grande des \
            pauvretés.", "Mère Teresa", "Amour"),
          ("Ce qui me bouleverse, ce n'est pas que tu m'aies menti, c'est \
            que désormais, je ne pourrai plus te croire.", "Friedrich \
            Nietzsche", "Amour"),
          ("Il n'y a pas d'au revoir pour nous. Peu importe où tu es, tu \
            seras toujours dans mon coeur.", "Gandhi", "Amour"),
          ("Des femmes peuvent très bien lier amitié avec un homme ; \
            mais pour la maintenir - il y faut peut-être le concours d'une \
            petite antipathie physique.", "Friedrich Nietzsche", "Amitié"),
          ("L'amitié sans confiance, c'est une fleur sans parfum.", "\
            Laure Conan", "Amitié"),
          ("L'amitié est une forme d'égalité comparable à la justice. \
            Chacun rend à l'autre des bienfaits semblables à ceux qu'il a \
            reçus.", "Aristote", "Amitié"),
          ("L'amitié nous fait sortir de nous-mêmes et ouvre ce \
            « nous-mêmes » sur des horizons infinis.", "Roland Poupon", \
            "Amitié"),
          ("Les riches ne se lient jamais d'amitié sincère avec \
            les pauvres.", "Massa Makan Diabaté", "Am itié"),
          ("La vie sans musique est tout simplement une erreur, une fatigue, \
            un exil.", "Friedrich Nietzsche", "Vie"),
          ("Soit A un succès dans la vie. Alors A = x + y + z, où x = \
            travailler, y = s'amuser, z = se taire.", "Albert Einstein", "Vie"),
          ("La vie est un défi à relever, un bonheur à mériter, une aventure \
            à tenter.", "Mère Teresa", "Vie"),
          ("La vie sans religion est une vie sans principe, et une vie sans \
            principe est comme un bateau sans gouvernail.", "Gandhi", "Vie"),
          ("Il y a deux moyens d'oublier les tracas de la vie : la musique et \
            les chats.", "Albert Schweitzer", "Vie"),
          ("L'ennui dans ce monde, c'est que les idiots sont sûrs d'eux et \
            les gens sensés pleins de doutes.", "Bertrand Russel", "Gens"),
          ("Vivre est la chose la plus rare. La plupart des gens se contente \
            d'exister.", "Oscar Wilde", "Vie"),
          ("Dieu a créé les gens en technicolor. Dieu n'a jamais fait de \
            différence entre un noir, un blanc, un bleu, un vert ou un rose.", \
            "Bob Marley", "Gens"),
          ("Les gens d'exceptions ne vivent pas les conformités morales ; \
            ils les créent. Et on les applique.", "Guy Parent", "Gens"),
          ("Si tu juges les gens tu n'as pas le temps de les aimer.", "Mère \
            Teresa", "Gens"),
          ("Le succès est un mauvais professeur. Il pousse les gens \
            intelligents à croire qu'ils sont infaillibles.", "Bill Gates", \
            "Gens"),
          ("Il y a des gens qui vous laissent tomber un pot de fleurs sur \
            la tête d'un cinquième étage et qui vous disent : je vous offre \
            ces roses.", "Victor Hugo", "Gens"),
          ("L'honnêteté, la sincérité, la simplicité, l'humilité, la \
            générosité, l'absence de vanité, la capacité à servir les autres \
            - qualités à la portée de toutes les âmes- sont les véritables \
            fondations de notre vie spirituelle.", "Nelson Mandela", "Vie"),
          ("Savoir écouter, c'est posséder, outre le sien, le cerveau des \
            autres.", "Léonard De Vinci", "Gens"),
          ("Y a des gens qui ont des enfants parce qu'ils n'ont pas les \
            moyens de s'offrir un chien.", "Coluche", "Gens"),
          ("Mesdames, un conseil. Si vous cherchez un homme beau, riche et \
            intelligent... prenez-en trois !", "Coluche", "Amour"),
          ("Certains ont l'air honnête, mais quand ils te serrent la main, \
            tu as intérêt à recompter tes doigts.", "Coluche", "Gens"),
          ("L'homme ordinaire est exigeant avec les autres. L'homme \
            exceptionnel est exigeant avec lui-même.", "Marc Aurèle", "Gens"),
          ("Si je devais recommencer ma vie, je n'y voudrais rien changer ; \
            seulement j'ouvrirais un peu plus grand les yeux.", \
            "Jules Renard", "Vie"),
          ("Il n'y a que deux façons de vivre sa vie : l'une en faisant comme \
            si rien n'était un miracle, l'autre en faisant comme si tout était \
            un miracle.", "Albert Einstein", "Vie"),
          ("Le travail éloigne de nous trois grands maux : l'ennui, le vice \
            et le besoin.", "Voltaire", "Travail"),
          ("Le domaine de la liberté commence là où s'arrête le travail \
            déterminé par la nécessité.", "Karl Marx", "Travail"),
          ("Plus je connais les gens, plus j'aime les chiens.", "Vladimir \
            Poutine", "Gens"),
          ("Vous pouvez faire beaucoup plus avec des armes et de la \
            politesse que juste de la politesse.", "Vladimir Poutine", "Vie"),
          ("Travail avec courage et persévérance, car la ténacité permet \
            d'atteindre l'excellence !", "Didier Court", "Travail"),
          ("Sachez vous éloigner car, lorsque vous reviendrez à votre \
            travail, votre jugement sera plus sûr.", "Léonard De Vinci", \
            "Travail"),
          ("Il n'y a point de travail honteux.", "Socrate", "Travail"),
          ("Construire peut être le fruit d'un travail long et acharné. \
            Détruire peut être l'oeuvre d'une seule journée.", "Winston \
            Churchill", "Travail"),
          ("Je choisis une personne paresseuse pour un travail difficile, \
            car une personne paresseuse va trouver un moyen facile de le \
            faire.", "Bill Gates", "Travail"),
          ("Un pessimiste voit la difficulté dans chaque opportunité, un \
            optimiste voit l'opportunité dans chaque difficulté.", "Winston \
            Churchill", "Vie"),
          ("Une pomme par jour éloigne le médecin, pourvu que l'on vise \
            bien.", "Winston Churchill", "Autre"),
          ("Si vous désirez la sympathie des masses, vous devez leur dire les \
            choses les plus stupides et les plus crues.", "Gens", \
            "Adolf Hitler"),
          ("Nous devons apprendre à vivre ensemble comme des frères, sinon \
            nous allons mourir tous ensemble comme des idiots.", "Martin \
            Luther King", "Autre"),
          ("Christophe Colomb fut le premier socialiste : il ne savait pas \
            où il allait, il ignorait où il se trouvait... et il faisait tout \
            ça aux frais du contribuable.", "Winston Churchill", "Autre"),
          ("Je suis prêt à rencontrer mon Créateur. Quant à savoir s'il est \
            préparé à l'épreuve de me voir, c'est une autre histoire.", \
            "Winston Churchill", "Autre"),
          ("La drogue a fait cent morts en France l'année dernière, l'alcool \
            cinquante mille ! Choisis ton camp, camarade !", "Coluche", \
            "Autre"),
          ("Des fois on a plus de contacts avec un chien pauvre qu'avec un \
            homme riche.", "Coluche", "Gens"),
          ("Les artichauts, c'est un vrai plat de pauvres. C'est le seul plat \
            que quand t'as fini de manger, t'en as plus dans ton assiette que \
            quand t'as commencé !", "Coluche", "Autre"),
          ("Les psychiatres, c'est très efficace. Moi, avant, je pissais au \
            lit, j'avais honte. Je suis allé voir un psychiatre, je suis \
            guéri. Maintenant, je pisse au lit, mais j'en suis fier.", \
            "Coluche", "Autre"),
          ("S'aimer soi-même est le début d'une histoire d'amour qui durera \
            toute une vie.", "Oscar Wilde", "Soi-même"),
          ("Le racisme est une manière de déléguer à l'autre le dégoût qu'on \
            a de soi-même.", "Robert Sabatier", "Soi-même"),
          ("Agis avec gentillesse, mais n'attends pas de la reconnaissance.", \
            "Confucius", "Soi-même"),
          ("Je ne cherche pas à connaître les réponses, je cherche à \
            comprendre les questions.", "Confucius", "Soi-même"),
          ("Nulle pierre ne peut être polie sans friction, nul homme ne peut \
            parfaire son expérience sans épreuve.", "Confucius", "Soi-même"),
          ("Examine si ce que tu promets est juste et possible, car la \
            promesse est une dette.", "Confucius", "Soi-même"),
          ("Ne vous souciez pas de n'être pas remarqué ; cherchez plutôt à \
            faire quelque chose de remarquable.", "Confucius", "Soi-même"),
          ("Soit le changement que tu veux voir dans le monde.", "Gandhi", \
            "Soi-même"),
          ("Vis comme si tu devais mourir demain, apprends comme si tu \
            devais vivre toujours.", "Gandhi", "Soi-même"),
          ("Quand tout va bien on peut compter sur les autres, quand tout \
            va mal on ne peut compter que sur sa famille.", \
            "Proverbe Chinois", "Famille"),
          ("Les enfants sont la chose la plus précieuse dans la vie. Un \
            parent doit faire tout ce qu'il peut pour donner à un enfant le \
            sens de la famille.", "Elvis Presley", "Famille"),
          ("Que pouvez-vous faire pour promouvoir la paix dans le monde ? \
            Rentrer chez vous et aimer votre famille !", "Mère Teresa", \
            "Famille"),
          ("L'amour d'une famille, le centre autour duquel tout gravite et \
            tout brille.", "Victor Hugo", "Famille"),
          ("Il n'y a point de tableau plus charmant que celui de la \
            famille.", "Jean Jacques Rousseau", "Famille"),
          ("La différence entre l'amour et l'argent, c'est que si on partage \
            son argent, il diminue, tandis que si on partage son amour, \
            il augmente. L'idéal étant d'arriver à partager son amour avec \
            quelqu'un qui a du pognon.", "Philippe Gelluk", "Argent"),
          ("Dans une société fondée sur le pouvoir de l'argent, tandis que \
            quelques poignées de riches ne savent être que des parasites, \
            il ne peut y avoir de liberté, réelle et véritable.", "Lénine", \
            "Argent"),
          ("Si on a perdu de l'argent, on n'a rien perdu ; si on a perdu les \
            amis, on a perdu la moitié de ce que l'on a et si on a perdu \
            l'espoir, on a tout perdu.", "Proverbe Albanais", "Argent"),
          ("La recherche a besoin d'argent dans deux domaines prioritaires : \
            le cancer et les missiles antimissiles. Pour les missiles \
            antimissiles, il y a les impôts. Pour le cancer, on fait la \
            quête.", "Pierre Desproges", "Argent"),
          ("L'argent est une richesse morte, les enfants sont une richesse \
            vivante.", "Proverbe Chinois", "Argent"),
          ("Avec tout l'argent du monde, on ne fait pas des hommes, mais \
            avec des hommes et qui aiment, on fait tout.", "Abbé Pierre", \
            "Argent"),
          ("Un sourire coûte moins cher que l'électricité, mais donne autant \
            de lumière.", "Abbé Pierre", "Argent"))

#Connect to MySQL
CONN = mysql.connector.connect(host="localhost", user="root")
cursor = CONN.cursor()
#Create database
cursor.execute("create database if not exists quotes_db;")
#Move to the database created
cursor.execute("use quotes_db")
#Create table will contain quotes
cursor.execute("create table if not exists quotes (id INT NOT NULL \
                AUTO_INCREMENT, quote TEXT NOT NULL, author VARCHAR(300) NOT \
                NULL, cat VARCHAR(150) NOT NULL, PRIMARY KEY (id));")
#Create table will contain saved quotes
cursor.execute("create table if not exists reg_quotes (id INT NOT NULL \
                AUTO_INCREMENT, quote TEXT NOT NULL, author VARCHAR(300) \
                NOT NULL, PRIMARY KEY (id));")
for quote in QUOTES:
    #Creation of a row for every quote
    cursor.execute("insert ignore into quotes (quote, author, cat) values \
                    (%s, %s, %s);", quote)
#Commit rows
CONN.commit()
