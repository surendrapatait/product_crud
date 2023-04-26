from flask import Flask ,request,render_template


app=Flask(__name__)
from model import Product

productList=list()
@app.route('/index')
def welcome_page():
    return render_template('index.html')


@app.route('/save',methods=['POST','GET'])
def save_update():
    message=''

    if request.method=='POST':
            formdata = request.form
            pid=int(formdata.get('prdid'))
            isduplicate=False
            for prod in productList:
                if prod.ProductId==pid:
                    prod.ProductName==formdata.get('prdnm')
                    prod.ProductQty == formdata.get('prdqty')
                    prod.ProductPrice == formdata.get('prdpr')
                    prod.ProducVendor==formdata.get('prdven')
                    isduplicate=True
                    break

            if isduplicate:
                message='Duplicate Product ...!/updated '
            else:
                prod=Product(id=formdata.get('prdid'),
                             pdnm=formdata.get('prdnm'),
                            pdqty=formdata.get('prdqty'),
                            pdpr=formdata.get('prdpr'),
                            pdven=formdata.get('prdven'))
                productList.append(prod)
                message='product added successfully'
    return render_template('add_product.html',message=message,product=Product())



@app.route('/show')
def show_product():
    return render_template('show_product.html',prodList=productList,product=Product())

@app.route('/delete/<int:pid>')
def delete(pid):
    product=None
    for prod in productList:
        if prod.ProductId==pid:
            product=prod
        productList.remove(product)
    return render_template('show_product.html',product=product)

@app.route('/edit/<int:pid>')
def edit(pid):
    product=None
    for prod in productList:
        if prod.ProductId==pid:
            product=prod
    return render_template('add_product.html',product=product)

@app.route('/search',methods=['POST','GET'])
def search():
    if request.method=='POST':
        formdata=request.form
        id=int(formdata.get('search'))
        for prod in productList:
            prod.ProductId==id
            return render_template('search.html',prod1=prod)
    return render_template('search.html', prod1=None)

if __name__=='__main__':
    app.run(debug=True)