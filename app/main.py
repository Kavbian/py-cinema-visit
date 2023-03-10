from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: list, hall_number: int, cleaner: str, movie: str
) -> None:
    list_of_customers = [
        Customer(customer["name"], customer["food"])
        for customer in customers
    ]
    hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()
    clean = Cleaner(cleaner)

    for customer in list_of_customers:
        cinema_bar.sell_product(customer.food, customer)

    hall.movie_session(movie, list_of_customers, clean)
