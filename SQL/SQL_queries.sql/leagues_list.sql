select id,
    name,
    country_name
from leagues_info
where country_name in { countries }
    and name in { leagues }