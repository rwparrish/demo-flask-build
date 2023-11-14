from config import app, db #need app context in order to seed database - why?
from models.models import *


with app.app_context():
    
    # clear the database
    Genre.query.delete()
    Designer.query.delete()
    Game.query.delete()
    db.session.commit()
    print("db cleared")
    
    # Create genres
    strategy = Genre(name="Strategy")  
    family = Genre(name="Family")
    party = Genre(name="Party")
    cooperative = Genre(name="Cooperative")
    deck_building = Genre(name="Deck Building")

    # Create designers
    reiner_knizia = Designer(name="Reiner Knizia")
    mattel = Designer(name="Mattel")
    philip_orbanes = Designer(name="Philip Orbanes") 
    richard_garfield = Designer(name="Richard Garfield")
    robert_daviau = Designer(name="Robert Daviau")

    # Create games  
    ticket_to_ride = Game(title="Ticket to Ride", players=2, time=60, designer=reiner_knizia, genre=strategy)
    uno = Game(title="Uno", players=4, time=30, designer=mattel, genre=party)
    monopoly = Game(title="Monopoly", players=4, time=180, designer=philip_orbanes, genre=family)
    pandemic = Game(title="Pandemic", players=4, time=45, designer=mattel, genre=cooperative)
    dominion = Game(title="Dominion", players=2, time=30, designer=richard_garfield, genre=deck_building)  
    betrayal_at_house_on_the_hill = Game(title="Betrayal at House on the Hill", players=6, time=60, designer=robert_daviau, genre=strategy)

    # Persist data 
    db.session.add_all([
    strategy, family, party, cooperative, deck_building, 
    reiner_knizia, mattel, philip_orbanes, richard_garfield, robert_daviau,
    ticket_to_ride, uno, monopoly, pandemic, dominion, betrayal_at_house_on_the_hill
    ])

    db.session.commit()

    print("Seeded database!")
        
    
