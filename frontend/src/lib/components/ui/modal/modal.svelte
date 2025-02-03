<script>
    import { tv } from "tailwind-variants";
    import { cn } from "$lib/utils";
    import { fade } from "svelte/transition";
    import Button from "../button/button.svelte";

    export let isOpen = false;
    export let message = "";
    export let onClose = () => {};

    const modalStyles = tv({
        slots: {
            overlay: cn(
                "fixed inset-0 bg-black/50 backdrop-blur-sm",
                "flex items-center justify-center z-50",
            ),
            container: cn(
                "bg-gray-900 rounded-lg p-6 shadow-xl",
                "border border-gray-800 max-w-md w-full mx-4",
            ),
            header: "text-xl font-medium text-gray-200 mb-4",
            message: "text-gray-200 text-lg mb-4",
        },
    });
</script>

{#if isOpen}
    <div class={modalStyles.slots.overlay} transition:fade>
        <div class={modalStyles.slots.container}>
            <h2 class={modalStyles.slots.header}>Unable to submit order</h2>
            <p class={modalStyles.slots.message}>{message}</p>
            <Button variant="destructive" size="default" on:click={onClose}>
                Close</Button
            >
        </div>
    </div>
{/if}
