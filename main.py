import view
import model
import controller

model = model.Model(25, 25)
view = view.View(model.rows, model.cols)
controller = controller.Controller(model, view)

view.create_canvas()
view.set_callback(controller.click);
view.render([], [], [])
view.start()
view.c()








