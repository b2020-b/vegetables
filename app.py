from flask import Flask, request, jsonify, render_template
import pymysql
from datetime import datetime

app = Flask(__name__)

# 数据库连接配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'vegetable',
    'charset': 'utf8mb4'
}

# 获取数据库连接
def get_db():
    return pymysql.connect(**db_config)

# 首页路由
@app.route('/')
def index():
    return render_template('index.html')

# 添加蔬菜
@app.route('/api/vegetable', methods=['POST'])
def add_vegetable():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        sql = "INSERT INTO vegetables (name, price) VALUES (%s, %s)"
        cursor.execute(sql, (data['name'], data['price']))
        conn.commit()
        return jsonify({'message': '添加成功'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# 获取所有蔬菜
@app.route('/api/vegetables', methods=['GET'])
def get_vegetables():
    conn = get_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        cursor.execute("SELECT * FROM vegetables")
        vegetables = cursor.fetchall()
        return jsonify(vegetables)
    finally:
        cursor.close()
        conn.close()

# 记录销售
@app.route('/api/sale', methods=['POST'])
def add_sale():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    
    try:
        sql = "INSERT INTO sales (vegetable_id, quantity, sale_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (data['vegetable_id'], data['quantity'], datetime.now().date()))
        conn.commit()
        return jsonify({'message': '销售记录添加成功'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

# 获取销售统计
@app.route('/api/sales/analysis', methods=['GET'])
def get_sales_analysis():
    conn = get_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        sql = """
        SELECT 
            v.name, 
            DATE_FORMAT(s.sale_date, '%Y-%m-%d') as sale_date, 
            SUM(s.quantity) as total_quantity,
            ROUND(SUM(s.quantity * v.price), 2) as total_amount
        FROM sales s
        JOIN vegetables v ON s.vegetable_id = v.id
        GROUP BY v.name, s.sale_date
        ORDER BY s.sale_date DESC, v.name
        """
        cursor.execute(sql)
        analysis = cursor.fetchall()
        
        for item in analysis:
            item['total_amount'] = float(item['total_amount']) if item['total_amount'] else 0
            item['total_quantity'] = int(item['total_quantity']) if item['total_quantity'] else 0
            
        return jsonify(analysis)
    except Exception as e:
        print(f"Error in sales analysis: {str(e)}")
        return jsonify([])
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(debug=True) 