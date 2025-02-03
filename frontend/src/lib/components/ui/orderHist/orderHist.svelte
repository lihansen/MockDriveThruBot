<script>
    import { tv } from "tailwind-variants";
    import { cn } from "$lib/utils";
    import Item from "./item.svelte";
    import orderHistIcon from "$lib/components/icons/orderHistIcon.svg";

    export let orders = [];

    const historyStyles = tv({
        slots: {
            container: cn(
                "my-8",
                "bg-gray-900/60 backdrop-blur-sm rounded-xl p-6",
                "shadow-[0_4px_12px_rgba(0,0,0,0.3)]",
                "hover:shadow-[0_8px_16px_rgba(0,0,0,0.6)]",
                "transition-all duration-200 ease-in-out",
            ),
            header: cn(
                "text-xl font-medium text-gray-200 mb-4",
                "flex items-center gap-2",
            ),
            icon: "w-8 h-8",
            content: "space-y-3 ",
        },
    });
</script>

<div class={historyStyles.slots.container}>
    <h3 class={historyStyles.slots.header}>
        <img
            src={orderHistIcon}
            alt="Order History"
            class={historyStyles.slots.icon}
        />
        Order History
    </h3>
    <div class={historyStyles.slots.content}>
        {#each orders as order}
            <Item
                orderId={order.orderId}
                burgers={order.burgers}
                fries={order.fries}
                drinks={order.drinks}
            />
        {/each}
    </div>
</div>
