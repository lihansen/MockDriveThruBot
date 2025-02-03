<script>
    import { tv } from "tailwind-variants";
    import { cn } from "$lib/utils";

    export let totalBurgers = 0;
    export let totalFries = 0;
    export let totalDrinks = 0;

    const totalStyles = tv({
        slots: {
            container: "grid grid-cols-3 gap-8 w-full",
            item: cn(
                "flex flex-col-reverse gap-1",
                "border border-gray-800 p-4 rounded-lg",
                "bg-gray-900/50 backdrop-blur-sm",
                "shadow-[0_4px_12px_rgba(0,0,0,0.3)]",
                "hover:shadow-[0_8px_16px_rgba(0,0,0,0.6)]",
                "transition-all duration-200 ease-in-out",
            ),
            label: "text-base/7 text-gray-300",
            value: "text-4xl font-semibold tracking-tight text-white",
        },
    });
</script>

<div class={totalStyles.slots.container}>
    <div class={totalStyles.slots.item}>
        <dt class={totalStyles.slots.label}>Total # of Burgers</dt>
        <dd class={totalStyles.slots.value}>
            {totalBurgers}
        </dd>
    </div>
    <div class={totalStyles.slots.item}>
        <dt class={totalStyles.slots.label}>Total # of Fries</dt>
        <dd class={totalStyles.slots.value}>
            {totalFries}
        </dd>
    </div>
    <div class={totalStyles.slots.item}>
        <dt class={totalStyles.slots.label}>Total # of drinks</dt>
        <dd class={totalStyles.slots.value}>
            {totalDrinks}
        </dd>
    </div>
</div>
