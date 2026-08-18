def schema_to_ddl(d):
    return ", ".join(f"`{c}` {t}" for c, t in d.items())


TABLE_SCHEMAS = {
    # ── dimensions ──────────────────────────────────────────────────────
    "locations": {
        "location_id": "BIGINT",
        "location_code": "STRING",
        "name": "STRING",
        "type": "STRING",
        "street": "STRING",
        "city": "STRING",
        "region": "STRING",
        "postal_code": "STRING",
        "latitude": "DOUBLE",
        "longitude": "DOUBLE",
        "phone": "STRING",
        "email": "STRING",
        "manager_id": "BIGINT",
        "number_of_bays": "BIGINT",
        "area_m2": "BIGINT",
        "opening_date": "DATE",
        "is_active": "BOOLEAN",
    },
    "employees": {
        "employee_id": "BIGINT",
        "employee_code": "STRING",
        "first_name": "STRING",
        "last_name": "STRING",
        "national_id": "STRING",
        "position": "STRING",
        "location_id": "BIGINT",
        "hire_date": "DATE",
        "termination_date": "DATE",
        "hourly_rate": "DOUBLE",
        "is_active": "BOOLEAN",
    },
    "customers": {
        "customer_id": "BIGINT",
        "customer_code": "STRING",
        "customer_type": "STRING",
        "first_name": "STRING",
        "last_name": "STRING",
        "company_name": "STRING",
        "tax_id": "STRING",
        "email": "STRING",
        "phone": "STRING",
        "city": "STRING",
        "postal_code": "STRING",
        "registration_date": "DATE",
        "preferred_location_id": "BIGINT",
        "marketing_consent": "BOOLEAN",
    },
    "vehicles": {
        "vehicle_id": "BIGINT",
        "customer_id": "BIGINT",
        "make": "STRING",
        "model": "STRING",
        "year": "BIGINT",
        "vin": "STRING",
        "registration_number": "STRING",
        "fuel_type": "STRING",
        "engine_displacement": "DOUBLE",
        "horsepower": "BIGINT",
        "color": "STRING",
        "mileage_km": "BIGINT",
        "first_registration_date": "DATE",
    },
    "products": {
        "product_id": "BIGINT",
        "product_code": "STRING",
        "name": "STRING",
        "category": "STRING",
        "manufacturer": "STRING",
        "purchase_price_net": "DOUBLE",
        "sale_price_net": "DOUBLE",
        "vat_rate": "BIGINT",
        "unit": "STRING",
        "weight_kg": "DOUBLE",
        "min_stock_level": "BIGINT",
        "is_active": "BOOLEAN",
    },
    "services": {
        "service_id": "BIGINT",
        "service_code": "STRING",
        "name": "STRING",
        "category": "STRING",
        "min_price_net": "BIGINT",
        "max_price_net": "BIGINT",
        "estimated_time_min": "BIGINT",
        "is_active": "BOOLEAN",
    },
    "suppliers": {
        "supplier_id": "BIGINT",
        "supplier_code": "STRING",
        "name": "STRING",
        "tax_id": "STRING",
        "city": "STRING",
        "address": "STRING",
        "postal_code": "STRING",
        "phone": "STRING",
        "email": "STRING",
        "contact_person": "STRING",
        "payment_terms_days": "BIGINT",
        "min_order_value": "DOUBLE",
        "is_active": "BOOLEAN",
    },
    # ── facts ────────────────────────────────────────────────────────────








    "work_orders": {
        "work_order_id": "BIGINT",
        "work_order_code": "STRING",
        "location_id": "BIGINT",
        "customer_id": "BIGINT",
        "vehicle_id": "BIGINT",
        "mechanic_id": "BIGINT",
        "reception_date": "DATE",
        "completion_date": "DATE",
        "status": "STRING",
        "mileage_at_reception": "BIGINT",
        "customer_notes": "STRING",
        "year": "INT",
        "month": "INT",
    },

    "work_order_items": {
        "wo_item_id": "BIGINT",
        "work_order_id": "BIGINT",
        "item_type": "STRING",
        "service_id": "BIGINT",
        "product_id": "BIGINT",
        "quantity": "BIGINT",
        "unit_price_net": "DOUBLE",
        "value_net": "DOUBLE",
        "vat_rate": "BIGINT",
        "value_gross": "DOUBLE",
        "discount_percent": "BIGINT",
    },




    "sales_transactions": {
        "transaction_id": "BIGINT",
        "transaction_code": "STRING",
        "location_id": "BIGINT",
        "customer_id": "BIGINT",
        "employee_id": "BIGINT",
        "transaction_date": "DATE",
        "payment_method": "STRING",
        "receipt_number": "STRING",
        "year": "INT",
        "month": "INT",
    },




    "sales_items": {
        "sales_item_id": "BIGINT",
        "transaction_id": "BIGINT",
        "product_id": "BIGINT",
        "quantity": "BIGINT",
        "unit_price_net": "DOUBLE",
        "discount_percent": "BIGINT",
        "value_net": "DOUBLE",
        "vat_rate": "BIGINT",
        "value_gross": "DOUBLE",
    },



    "invoices": {
        "invoice_id": "BIGINT",
        "invoice_code": "STRING",
        "document_type": "STRING",
        "source_type": "STRING",
        "source_id": "BIGINT",
        "customer_id": "BIGINT",
        "location_id": "BIGINT",
        "issue_date": "DATE",
        "sale_date": "DATE",
        "payment_due_date": "DATE",
        "value_net": "DOUBLE",
        "value_vat": "DOUBLE",
        "value_gross": "DOUBLE",
        "status": "STRING",
        "year": "INT",
        "month": "INT",
    },



    "payments": {
        "payment_id": "BIGINT",
        "invoice_id": "BIGINT",
        "payment_date": "DATE",
        "amount": "DOUBLE",
        "payment_method": "STRING",
        "status": "STRING",
        "transaction_number": "STRING",
        "year": "INT",
        "month": "INT",
    },



    "inventory_movements": {
        "movement_id": "BIGINT",
        "product_id": "BIGINT",
        "location_id": "BIGINT",
        "movement_type": "STRING",
        "quantity": "BIGINT",
        "movement_date": "DATE",
        "source_document": "STRING",
        "document_number": "STRING",
        "value_net": "DOUBLE",
        "notes": "STRING",
        "year": "INT",
        "month": "INT",
    },



    "appointments": {
        "appointment_id": "BIGINT",
        "customer_id": "BIGINT",
        "vehicle_id": "BIGINT",
        "location_id": "BIGINT",
        "service_id": "BIGINT",
        "booking_date": "DATE",
        "appointment_date": "DATE",
        "status": "STRING",
        "booking_channel": "STRING",
        "notes": "STRING",
        "year": "INT",
        "month": "INT",
    },




    "purchase_orders": {
        "po_id": "BIGINT",
        "po_code": "STRING",
        "supplier_id": "BIGINT",
        "location_id": "BIGINT",
        "order_date": "DATE",
        "planned_delivery_date": "DATE",
        "actual_delivery_date": "DATE",
        "value_net": "DOUBLE",
        "value_gross": "DOUBLE",
        "status": "STRING",
        "year": "INT",
    },



    "purchase_order_items": {
        "po_item_id": "BIGINT",
        "po_id": "BIGINT",
        "product_id": "BIGINT",
        "quantity_ordered": "BIGINT",
        "quantity_delivered": "BIGINT",
        "unit_price_net": "DOUBLE",
        "value_net": "DOUBLE",
    },



    "customer_feedback": {
        "feedback_id": "BIGINT",
        "customer_id": "BIGINT",
        "location_id": "BIGINT",
        "work_order_id": "BIGINT",
        "feedback_date": "DATE",
        "rating": "BIGINT",
        "comment": "STRING",
        "category": "STRING",
        "channel": "STRING",
    },



    "loyalty_program": {
        "loyalty_id": "BIGINT",
        "customer_id": "BIGINT",
        "event_date": "DATE",
        "event_type": "STRING",
        "points": "BIGINT",
        "description": "STRING",
        "balance_after": "BIGINT",
        "tier": "STRING",
    },




    "employee_schedules": {
        "schedule_id": "BIGINT",
        "employee_id": "BIGINT",
        "date": "DATE",
        "start_hour": "BIGINT",
        "end_hour": "BIGINT",
        "shift_type": "STRING",
        "overtime_hours": "BIGINT",
        "attendance": "STRING",
    },
}

# fact tables that carry partition columns in their parquet directory structure
PARTITIONED_TABLES = {
    "work_orders": ["year", "month"],
    "sales_transactions": ["year", "month"],
    "invoices": ["year", "month"],
    "payments": ["year", "month"],
    "inventory_movements": ["year", "month"],
    "appointments": ["year", "month"],
    "purchase_orders": ["year"],
}

print(f"Schemas loaded: {len(TABLE_SCHEMAS)} tables")