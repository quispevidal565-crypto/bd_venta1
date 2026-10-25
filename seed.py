
from decimal import Decimal

from app import create_app
from app.extensions import db
from app.models import Usuario, Cliente, Producto, Venta, DetalleVenta

app = create_app()

with app.app_context():
    if not Usuario.query.filter_by(username="admin").first():
        usuario = Usuario(username="admin", rol="administrador")
        usuario.set_password("Admin123!")
        db.session.add(usuario)

    if not Cliente.query.filter_by(email="ana@example.com").first():
        ana = Cliente(
            nombre="Ana Pérez",
            email="ana@example.com",
            telefono="70000001"
        )
        db.session.add(ana)

    if not Producto.query.filter_by(
        descripcion="Teclado mecánico"
    ).first():
        teclado = Producto(
            descripcion="Teclado mecánico",
            precio=Decimal("45.50"),
            stock=20
        )
        db.session.add(teclado)

    if not Producto.query.filter_by(
        descripcion="Mouse inalámbrico"
    ).first():
        mouse = Producto(
            descripcion="Mouse inalámbrico",
            precio=Decimal("18.00"),
            stock=35
        )
        db.session.add(mouse)

    db.session.commit()

    ana = Cliente.query.filter_by(email="ana@example.com").first()
    teclado = Producto.query.filter_by(
        descripcion="Teclado mecánico"
    ).first()
    mouse = Producto.query.filter_by(
        descripcion="Mouse inalámbrico"
    ).first()

    if ana and not ana.ventas:
        venta = Venta(cliente=ana)
        venta.detalles.extend([
            DetalleVenta(
                producto=teclado,
                cantidad=1,
                precio_unitario=Decimal("45.50")
            ),
            DetalleVenta(
                producto=mouse,
                cantidad=2,
                precio_unitario=Decimal("18.00")
            )
        ])
        db.session.add(venta)
        db.session.commit()

    print("Datos de prueba cargados correctamente.")
    print("Usuarios:", Usuario.query.count())
    print("Clientes:", Cliente.query.count())
    print("Productos:", Producto.query.count())
    print("Ventas:", Venta.query.count())
    print("Detalles de venta:", DetalleVenta.query.count())
