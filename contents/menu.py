from typing import Optional

#メニュー一件分のデータの箱
class Menu:
    def __init__(self,id: int,name: str,category: str,price: int,description: Optional[str],image: str) -> None:
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.image = image
    
#初期データ（データベースの代わりとなるリスト)　初期のメニューリスト！
menus = [
    Menu(1, "ブレンドコーヒー", "ドリンク", 450, "深煎りの豆を使った定番コーヒー", "https://placehold.jp/6f4e37/ffffff/300x200.png?text=Coffee"),
    Menu(2, "カフェラテ", "ドリンク", 520, "エスプレッソとたっぷりのミルク", "https://placehold.jp/c8a27a/ffffff/300x200.png?text=Latte"),
    Menu(3, "抹茶ラテ", "ドリンク", 580, "宇治抹茶を使ったほろ苦いラテ", "https://placehold.jp/7a9a4a/ffffff/300x200.png?text=Matcha"),
    Menu(4, "ミックスサンド", "フード", 680, "たまごとハムの2種類のサンド", "https://placehold.jp/e0b050/ffffff/300x200.png?text=Sandwich"),
    Menu(5, "ナポリタン", "フード", 850, "昔ながらの喫茶店の味", "https://placehold.jp/c0392b/ffffff/300x200.png?text=Napolitan"),
    Menu(6, "チーズケーキ", "デザート", 480, "濃厚なベイクドチーズケーキ", "https://placehold.jp/f2d16b/333333/300x200.png?text=Cheesecake"),
    Menu(7, "プリン", "デザート", 400, "固めの昔ながらのプリン", "https://placehold.jp/d9a05b/ffffff/300x200.png?text=Pudding"),
]

def get_allmenus():
    return menus

#目的のメニューを取得する関数。
def get_target_menu(menu_id : int):
    for menu in menus:
        if menu.id == menu_id:
            return menu
    return None

#カテゴリが一致したmenuを返す
def find_menu_filter_by_category(category:str):
    filtered_menu = []
    for menu in menus:
        if category == menu.category:
            filtered_menu.append(menu)
    return filtered_menu


def find_menu_filter_by_maxprice(max_price : int):
    filtered_menu = []
    for menu in menus:
        if max_price >= menu.price:
            filtered_menu.append(menu)
    return filtered_menu

#内部では新規入門の追加。クライアントには、新規追加したメニュのリクエストボディにあるデータを返す。
# リクエストのJSONはFastAPIによってPythonの辞書（dict）に変換される。
# create関数にはその辞書が渡されるため、値は .get() または ["キー名"] で取得する。
def create(menu_create):
    new_menu = Menu(
        id=len(menus) + 1,
        name=menu_create.get("name", ""),
        category=menu_create.get("category", ""),
        price=menu_create.get("price", 0),
        description=menu_create.get("description"),
        image=menu_create.get("image", ""),
    )
    menus.append(new_menu)
    return new_menu

def update(id:int,menu_update):
    #リクエスト時に取得したリクエストボディのデータがあれば、指定のidのメニューのデータに上書きする。
    #
    for menu in menus:
        if menu.id == id:
            menu.name = menu_update.get("name",menu.name)
            menu.category = menu_update.get("category",menu.category)
            menu.price = menu_update.get("price",menu.price)
            menu.description = menu_update.get("description",menu.description)
            menu.image = menu_update.get("image",menu.image)
        return menu
    return None

def delete(id):
    for menu in menus:
        if menu.id == id:
            menus.remove(menu)
            return menu
    return None