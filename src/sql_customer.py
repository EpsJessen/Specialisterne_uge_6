from sql_user import Sql_user


class Sql_customer(Sql_user):
    basket: list[tuple[int, int]]

    def __init__(self, user: str, password: str, schema: str = "bikes"):
        super().__init__(user=user, password=password, schema=schema)

    def get_own_info(self):
        return super().get_info("CALL customer_info_self();")

    def change_fist_name(self, new_name):
        return super().make_change(f"CALL customer_change_first_name('{new_name}');")

    def add_to_basket(self, product_id: int, amount: int):
        if amount < 1:
            return -1
        available = super().get_info(
            f"""
                                     SELECT SUM(quantity)
                                     FROM bikes.stocks
                                     WHERE product_id = {product_id}
                                     """
        )
        if available >= amount:
            self.basket.append(product_id, amount)
            return 1
        else:
            return -1

    def buy_basket(store_id):
        success, stores = super().get_info("SELECT store_id FROM stores")
        if not success:
            return 0
        if store_id not in stores["store_id"]:
            return -1


def main():
    mary = Sql_customer(user="1", password="PASS")
    print(mary.get_own_info()[1])
    print("Wait, that's not my name!")
    print(mary.change_fist_name("Mary"))
    print(mary.get_own_info()[1])
    print("That's better :)")


if __name__ == "__main__":
    main()
