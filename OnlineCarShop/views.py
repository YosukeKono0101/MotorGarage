from operator import or_
from re import X
from turtle import st
from unicodedata import category
from django.shortcuts import redirect, render
from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .model import Category, Item, Order
from .forms import PlaceOrderForm
from . import db
from sqlalchemy import or_


bp=Blueprint('main',__name__)

@bp.route('/')
def index():
    categories = Category.query.order_by(Category.id).all()
    feture_item = Item.query.filter(or_(Item.id == 1,Item.id == 4,Item.id == 7))
    return render_template('index.html',categories = categories,feture_item=feture_item)

@bp.route('/category/<int:categoryid>/')
def category(categoryid):
    categories = Category.query.filter(Category.id == categoryid).first()
    categoryItem = Item.query.filter(Item.category_id == categoryid )
    return render_template('category.html',items=categoryItem,categories=categories)

@bp.route('/item/<int:itemid>')
def item(itemid):
    item = Item.query.get(itemid)
    categories = Category.query.filter(Category.id == item.category_id).first()
    return render_template('Item.html',item=item,categories=categories)

#search 
@bp.route('/items/')
def search():
    search = request.args.get('search')
    search = '%{}%'.format(search)
    item = Item.query.filter(Item.description.like(search)).all()
    print(item)

    return render_template('CategoryItems.html', item = item)

#order
@bp.route('/order', methods = ['POST','GET'])
def order():

    item_id = request.values.get('item_id')

    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
    else:
        order = None

    if order is None:
        order = Order(status = False, firstname='', lastname='', email='', address='',totalcost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    if order is not None:
        for item in order.items:
            totalprice = totalprice + item.price
    
    # are we adding an item?
    if item_id is not None and order is not None:
        item = Item.query.get(item_id)
        if item not in order.items:
            try:
                order.items.append(item)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.order'))
        else:
            flash('item already in basket')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)

#removeorder
@bp.route('/removeorder/')
def removeorder():
    if 'order_id' in session:
        del session['order_id']
        flash('All items are removed')
    return redirect(url_for('main.index'))

#removeitem
@bp.route('/removeitem', methods=['POST'])
def removeitem():
    id = request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        item_to_delete = Item.query.get(id)
        try:
            order.items.remove(item_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Items could not be removed due to some issues..'
    return redirect(url_for('main.order'))


#PlaceOrder
@bp.route('/placeorder', methods=['POST','GET'])
def placeorder():
    form = PlaceOrderForm()
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])

        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.address = form.address.data
            total_cost = 0
            for item in order.items:
                total_cost = total_cost + item.price
            order.total_cost = total_cost
            try:
                db.session.commit()
                del session['order_id']            
                flash("Thank you for your purchase. We will contact you once we confirm your order!")
                return redirect(url_for('main.index'))
            except:
                return 'The order is not completed due to some issues..'
    return render_template('OrderingPage.html', form = form)  