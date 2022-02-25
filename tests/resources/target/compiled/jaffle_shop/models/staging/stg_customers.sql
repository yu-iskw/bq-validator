with source as (
    select * from `your-project`.`jaffle_shop`.`raw_customers`

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed
