<script>
    import { tv } from "tailwind-variants";
    import { cn } from "$lib/utils";

    export let orderId;
    export let burgers;
    export let fries;
    export let drinks;

    const itemStyles = tv({
        slots: {
            container: cn(
                "flex items-center justify-between p-4",
                "bg-gray-800/50 backdrop-blur-sm rounded-lg",
                "border-gray-700/50",
                "hover:bg-gray-800/60 transition-all duration-200 group",
            ),
            idContainer: "flex-shrink-0",
            idBadge: cn(
                "flex items-center justify-center",
                "w-10 h-10 rounded-full",
                "bg-indigo-500/10 text-indigo-400",
            ),
            details: "text-gray-300 font-medium ml-auto",
        },
    });

    function orderDetail(order) {
        let res = [];
        if (order.burgers) {
            if (order.burgers === 1) {
                res.push("1 Burger");
            } else {
                res.push(order.burgers + " Burgers");
            }
        }
        if (order.fries) {
            if (order.fries === 1) {
                res.push("1 Fry");
            } else {
                res.push(order.fries + " Fries");
            }
        }
        if (order.drinks) {
            if (order.drinks === 1) {
                res.push("1 Drink");
            } else {
                res.push(order.drinks + " Drinks");
            }
        }
        return res.join(", ");
    }
</script>

<div class={itemStyles.slots.container}>
    <div class={itemStyles.slots.idContainer}>
        <div class={itemStyles.slots.idBadge}>
            #{orderId}
        </div>
    </div>
    <div class={itemStyles.slots.details}>
        {orderDetail({ burgers, fries, drinks })}
    </div>
</div>
