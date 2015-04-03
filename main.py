import view
import model
import controller


model = model.Model(8, 8)
view = view.View(model.rows, model.cols)
controller = controller.Controller(model, view)


view.set_callback(controller.click);
view.render([], [])

view.c()








