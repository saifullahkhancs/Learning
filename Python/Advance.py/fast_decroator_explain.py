class MyApp:

    def __init__(self):
        self.routes = []

    def get(self, path):

        # This function is returned by app.get("/")
        def decorator(function):

            # Register the route
            self.routes.append({
                "method": "GET",
                "path": path,
                "handler": function
            })

            # Return the original function
            return function

        return decorator


app = MyApp()


async def root():
    return {
        "message": "Hello World"
    }


# This:
#
# @app.get("/")
# async def root():
#     ...

#
# is equivalent to:
#

decorator = app.get("/")

root = decorator(root)


print(app.routes)
