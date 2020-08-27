from flask import jsonify

class ProductService:

    def __init__(self, product_dao):
        self.product_dao = product_dao

    def create_product(self, product_info, db_connection):

        """

        상품등록 Service function

        Args:
            product_info  : AdminProductView.product_register로 받은 Parameter
            db_connection : DATABASE Connection Instance

        Returns:
            200: SUCCESS, (상품등록 완료)

        Author:
            sincerity410@gmail.com (이곤호)

        History:
            2020-08-25 (sincerity410@gmail.com) : 초기생성

        """

        product_id                 = self.product_dao.insert_product(db_connection)
        product_info['product_id'] = product_id
        self.product_dao.insert_product_detail(product_info, db_connection)

        return jsonify({'message': 'SUCCESS'}), 200

    def get_product_list(self, db_connection):

        """

        브랜디 서비스 페이지 > 상품 전체 리스트

        Args:
            연결된 db 객체

        Returns:
            상품 전체 리스트

        Authors:
            minho.lee0716@gmail.com(이민호)

        History:
            2020-08-25 (minho.lee0716@gmail.com) : 초기 생성

        """

        # 상품의 기준은 진열여부=True, 판매여부=True
        products = self.product_dao.select_product_list(db_connection)

        # 모든 상품을 리턴
        return products
