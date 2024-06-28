from .settings import project
import home_page, registration_page, login_page, shop_page, cart_page, admin_page

home_page.home_page.add_url_rule(
    rule = "/",
    view_func = home_page.render_home_page,
    methods = ["GET", "POST"]
)
registration_page.register_page.add_url_rule(
    rule= "/registration/",
    view_func= registration_page.render_registration,
    methods = ["GET", "POST"]
)

login_page.login_page.add_url_rule(
    rule= "/login/",
    view_func= login_page.render_login_page,
    methods = ["GET", "POST"]
)

shop_page.shop_page.add_url_rule(
    rule= "/shop/",
    view_func= shop_page.render_shop_page,
    methods = ["GET", "POST"]
)

cart_page.cart_page.add_url_rule(
    rule= "/cart/",
    view_func= cart_page.render_cart_page,
    methods = ["GET", "POST"]
)

admin_page.admin_page.add_url_rule(
    rule= "/admin/",
    view_func= admin_page.render_admin_page,
    methods = ["GET", "POST"]
)
project.register_blueprint(blueprint= registration_page.register_page)
project.register_blueprint(blueprint= login_page.login_page)
project.register_blueprint(blueprint= shop_page.shop_page)
project.register_blueprint(blueprint= cart_page.cart_page)
project.register_blueprint(blueprint = home_page.home_page)
project.register_blueprint(blueprint= admin_page.admin_page)