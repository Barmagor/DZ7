import export
import import_number
import view

def click():
    control=view.start()
    if control ==1:
        import_number.import_telephone()
    if control ==2:
        export.export_telephone()