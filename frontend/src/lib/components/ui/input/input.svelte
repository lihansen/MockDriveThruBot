<script lang="ts">
    import { tv } from "tailwind-variants";
    import { cn } from "$lib/utils";

    let placeholder =
        'Drive thru message:\nEx: "I would like one burger and an order of fries"\n     "Cancel order #2"';
    let rows = 4;
    export let message = "";

    const textareaStyle = tv({
        base: cn(
            "min-w-0 flex-auto rounded-md",
            "bg-white/5 px-3.5 py-2",
            "text-base text-white",
            "outline-1 -outline-offset-1 outline-white/10",
            "placeholder:text-gray-500",
            "focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-500",
            "shadow-[0_4px_12px_rgba(0,0,0,0.3)]",
            "hover:shadow-[0_8px_16px_rgba(0,0,0,0.6)]",
            "transition-all duration-200 ease-in-out",
        ),
    });
</script>

<textarea
    id="message"
    name="message"
    {rows}
    required
    bind:value={message}
    class={textareaStyle()}
    {placeholder}
></textarea>
