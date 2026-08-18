# ============================================================
# TABLE SCHEMAS (column -> Spark SQL type)
# Single source of truth for all car_workshop tables.
# Kept in sync with create_tables.sql.
#
# Usage:
#   from table_schemas import TABLE_SCHEMAS, PARTITIONED_TABLES, schema_to_ddl
#   spark.read.schema(schema_to_ddl(TABLE_SCHEMAS['locations'])).parquet(path)
#   spark.createDataFrame(pdf, schema=schema_to_ddl(TABLE_SCHEMAS['locations']))
# ============================================================

# ------------------------------------------------------------
# DIMENSIONS
# ------------------------------------------------------------

LOCATIONS_SCHEMA = {
    'location_id':     'BIGINT',
    'location_code':   'STRING',
    'name':            'STRING',
    'type':            'STRING',
    'street':          'STRING',
    'city':            'STRING',
    'region':          'STRING',
    'postal_code':     'STRING',
    'latitude':        'DOUBLE',
    'longitude':       'DOUBLE',
    'phone':           'STRING',
    'email':           'STRING',
    'manager_id':      'BIGINT',
    'number_of_bays':  'BIGINT',
    'area_m2':         'BIGINT',
    'opening_date':    'DATE',
    'is_active':       'BOOLEAN',
}

EMPLOYEES_SCHEMA = {
    'employee_id':      'BIGINT',
    'employee_code':    'STRING',
    'first_name':       'STRING',
    'last_name':        'STRING',
    'national_id':      'STRING',
    'position':         'STRING',
    'location_id':      'BIGINT',
    'hire_date':        'DATE',
    'termination_date': 'DATE',
    'hourly_rate':      'DOUBLE',
    'is_active':        'BOOLEAN',
}

CUSTOMERS_SCHEMA = {
    'customer_id':           'BIGINT',
    'customer_code':         'STRING',
    'customer_type':         'STRING',
    'first_name':            'STRING',
    'last_name':             'STRING',
    'company_name':          'STRING',
    'tax_id':                'STRING',
    'email':                 'STRING',
    'phone':                 'STRING',
    'city':                  'STRING',
    'postal_code':           'STRING',
    'registration_date':     'DATE',
    'preferred_location_id': 'BIGINT',
    'marketing_consent':     'BOOLEAN',
}

VEHICLES_SCHEMA = {
    'vehicle_id':              'BIGINT',
    'customer_id':             'BIGINT',
    'make':                    'STRING',
    'model':                   'STRING',
    'year':                    'BIGINT',
    'vin':                     'STRING',
    'registration_number':     'STRING',
    'fuel_type':               'STRING',
    'engine_displacement':     'DOUBLE',
    'horsepower':              'BIGINT',
    'color':                   'STRING',
    'mileage_km':              'BIGINT',
    'first_registration_date': 'DATE',
}

PRODUCTS_SCHEMA = {
    'product_id':         'BIGINT',
    'product_code':       'STRING',
    'name':               'STRING',
    'category':           'STRING',
    'manufacturer':       'STRING',
    'purchase_price_net': 'DOUBLE',
    'sale_price_net':     'DOUBLE',
    'vat_rate':           'BIGINT',
    'unit':               'STRING',
    'weight_kg':          'DOUBLE',
    'min_stock_level':    'BIGINT',
    'is_active':          'BOOLEAN',
}

SERVICES_SCHEMA = {
    'service_id':         'BIGINT',
    'service_code':       'STRING',
    'name':               'STRING',
    'category':           'STRING',
    'min_price_net':      'BIGINT',
    'max_price_net':      'BIGINT',
    'estimated_time_min': 'BIGINT',
    'is_active':          'BOOLEAN',
}

SUPPLIERS_SCHEMA = {
    'supplier_id':        'BIGINT',
    'supplier_code':      'STRING',
    'name':               'STRING',
    'tax_id':             'STRING',
    'city':               'STRING',
    'address':            'STRING',
    'postal_code':        'STRING',
    'phone':              'STRING',
    'email':              'STRING',
    'contact_person':     'STRING',
    'payment_terms_days': 'BIGINT',
    'min_order_value':    'DOUBLE',
    'is_active':          'BOOLEAN',
}

# ------------------------------------------------------------
# FACTS
# ------------------------------------------------------------

WORK_ORDERS_SCHEMA = {
    'work_order_id':        'BIGINT',
    'work_order_code':      'STRING',
    'location_id':          'BIGINT',
    'customer_id':          'BIGINT',
    'vehicle_id':           'BIGINT',
    'mechanic_id':          'BIGINT',
    'reception_date':       'DATE',
    'completion_date':      'DATE',
    'status':               'STRING',
    'mileage_at_reception': 'BIGINT',
    'customer_notes':       'STRING',
    'year':                 'INT',
    'month':                'INT',
}

WORK_ORDER_ITEMS_SCHEMA = {
    'wo_item_id':       'BIGINT',
    'work_order_id':    'BIGINT',
    'item_type':        'STRING',
    'service_id':       'BIGINT',
    'product_id':       'BIGINT',
    'quantity':         'BIGINT',
    'unit_price_net':   'DOUBLE',
    'value_net':        'DOUBLE',
    'vat_rate':         'BIGINT',
    'value_gross':      'DOUBLE',
    'discount_percent': 'BIGINT',
}

SALES_TRANSACTIONS_SCHEMA = {
    'transaction_id':   'BIGINT',
    'transaction_code': 'STRING',
    'location_id':      'BIGINT',
    'customer_id':      'BIGINT',
    'employee_id':      'BIGINT',
    'transaction_date': 'DATE',
    'payment_method':   'STRING',
    'receipt_number':   'STRING',
    'year':             'INT',
    'month':            'INT',
}

SALES_ITEMS_SCHEMA = {
    'sales_item_id':    'BIGINT',
    'transaction_id':   'BIGINT',
    'product_id':       'BIGINT',
    'quantity':         'BIGINT',
    'unit_price_net':   'DOUBLE',
    'discount_percent': 'BIGINT',
    'value_net':        'DOUBLE',
    'vat_rate':         'BIGINT',
    'value_gross':      'DOUBLE',
}

INVOICES_SCHEMA = {
    'invoice_id':       'BIGINT',
    'invoice_code':     'STRING',
    'document_type':    'STRING',
    'source_type':      'STRING',
    'source_id':        'BIGINT',
    'customer_id':      'BIGINT',
    'location_id':      'BIGINT',
    'issue_date':       'DATE',
    'sale_date':        'DATE',
    'payment_due_date': 'DATE',
    'value_net':        'DOUBLE',
    'value_vat':        'DOUBLE',
    'value_gross':      'DOUBLE',
    'status':           'STRING',
    'year':             'INT',
    'month':            'INT',
}

PAYMENTS_SCHEMA = {
    'payment_id':         'BIGINT',
    'invoice_id':         'BIGINT',
    'payment_date':       'DATE',
    'amount':             'DOUBLE',
    'payment_method':     'STRING',
    'status':             'STRING',
    'transaction_number': 'STRING',
    'year':               'INT',
    'month':              'INT',
}

INVENTORY_MOVEMENTS_SCHEMA = {
    'movement_id':     'BIGINT',
    'product_id':      'BIGINT',
    'location_id':     'BIGINT',
    'movement_type':   'STRING',
    'quantity':        'BIGINT',
    'movement_date':   'DATE',
    'source_document': 'STRING',
    'document_number': 'STRING',
    'value_net':       'DOUBLE',
    'notes':           'STRING',
    'year':            'INT',
    'month':           'INT',
}

APPOINTMENTS_SCHEMA = {
    'appointment_id':   'BIGINT',
    'customer_id':      'BIGINT',
    'vehicle_id':       'BIGINT',
    'location_id':      'BIGINT',
    'service_id':       'BIGINT',
    'booking_date':     'DATE',
    'appointment_date': 'DATE',
    'status':           'STRING',
    'booking_channel':  'STRING',
    'notes':            'STRING',
    'year':             'INT',
    'month':            'INT',
}

PURCHASE_ORDERS_SCHEMA = {
    'po_id':                 'BIGINT',
    'po_code':               'STRING',
    'supplier_id':           'BIGINT',
    'location_id':           'BIGINT',
    'order_date':            'DATE',
    'planned_delivery_date': 'DATE',
    'actual_delivery_date':  'DATE',
    'value_net':             'DOUBLE',
    'value_gross':           'DOUBLE',
    'status':                'STRING',
    'year':                  'INT',
}

PURCHASE_ORDER_ITEMS_SCHEMA = {
    'po_item_id':         'BIGINT',
    'po_id':              'BIGINT',
    'product_id':         'BIGINT',
    'quantity_ordered':   'BIGINT',
    'quantity_delivered': 'BIGINT',
    'unit_price_net':     'DOUBLE',
    'value_net':          'DOUBLE',
}

CUSTOMER_FEEDBACK_SCHEMA = {
    'feedback_id':   'BIGINT',
    'customer_id':   'BIGINT',
    'location_id':   'BIGINT',
    'work_order_id': 'BIGINT',
    'feedback_date': 'DATE',
    'rating':        'BIGINT',
    'comment':       'STRING',
    'category':      'STRING',
    'channel':       'STRING',
}

LOYALTY_PROGRAM_SCHEMA = {
    'loyalty_id':    'BIGINT',
    'customer_id':   'BIGINT',
    'event_date':    'DATE',
    'event_type':    'STRING',
    'points':        'BIGINT',
    'description':   'STRING',
    'balance_after': 'BIGINT',
    'tier':          'STRING',
}

EMPLOYEE_SCHEDULES_SCHEMA = {
    'schedule_id':    'BIGINT',
    'employee_id':    'BIGINT',
    'date':           'DATE',
    'start_hour':     'BIGINT',
    'end_hour':       'BIGINT',
    'shift_type':     'STRING',
    'overtime_hours': 'BIGINT',
    'attendance':     'STRING',
}

# ------------------------------------------------------------
# Master registry {table_name: schema_dict}
# ------------------------------------------------------------

TABLE_SCHEMAS = {
    'locations':             LOCATIONS_SCHEMA,
    'employees':             EMPLOYEES_SCHEMA,
    'customers':             CUSTOMERS_SCHEMA,
    'vehicles':              VEHICLES_SCHEMA,
    'products':              PRODUCTS_SCHEMA,
    'services':              SERVICES_SCHEMA,
    'suppliers':             SUPPLIERS_SCHEMA,
    'work_orders':          WORK_ORDERS_SCHEMA,
    'work_order_items':     WORK_ORDER_ITEMS_SCHEMA,
    'sales_transactions':   SALES_TRANSACTIONS_SCHEMA,
    'sales_items':          SALES_ITEMS_SCHEMA,
    'invoices':             INVOICES_SCHEMA,
    'payments':             PAYMENTS_SCHEMA,
    'inventory_movements':  INVENTORY_MOVEMENTS_SCHEMA,
    'appointments':         APPOINTMENTS_SCHEMA,
    'purchase_orders':      PURCHASE_ORDERS_SCHEMA,
    'purchase_order_items': PURCHASE_ORDER_ITEMS_SCHEMA,
    'customer_feedback':    CUSTOMER_FEEDBACK_SCHEMA,
    'loyalty_program':      LOYALTY_PROGRAM_SCHEMA,
    'employee_schedules':   EMPLOYEE_SCHEDULES_SCHEMA,
}

# Fact tables whose parquet layout / Delta tables are partitioned.
PARTITIONED_TABLES = {
    'work_orders':         ['year', 'month'],
    'sales_transactions':  ['year', 'month'],
    'invoices':            ['year', 'month'],
    'payments':            ['year', 'month'],
    'inventory_movements': ['year', 'month'],
    'appointments':        ['year', 'month'],
    'purchase_orders':     ['year'],
}


def schema_to_ddl(schema_dict):
    """Schema dict -> DDL string for spark.read.schema() / createDataFrame()."""
    return ', '.join(f'`{col}` {typ}' for col, typ in schema_dict.items())


def build_spark_schema(schema_dict):
    """Schema dict -> pyspark StructType (import deferred so this module works without pyspark)."""
    from pyspark.sql.types import (
        StructType, StructField, StringType, IntegerType, LongType,
        DoubleType, BooleanType, DateType, TimestampType,
    )
    type_map = {
        'STRING':    StringType(),
        'INT':       IntegerType(),
        'BIGINT':    LongType(),
        'DOUBLE':    DoubleType(),
        'BOOLEAN':   BooleanType(),
        'DATE':      DateType(),
        'TIMESTAMP': TimestampType(),
    }
    return StructType([
        StructField(col, type_map[typ.upper()], nullable=True)
        for col, typ in schema_dict.items()
    ])
