<script>
    import axios from "axios";
    import TotalSection from "../lib/components/ui/totalSec/totalSection.svelte";
    import Input from "$lib/components/ui/input/input.svelte";
    import OrderHist from "../lib/components/ui/orderHist/orderHist.svelte";
    import Button from "$lib/components/ui/button/button.svelte";
    import Modal from "$lib/components/ui/modal/modal.svelte";

    import { tv } from "tailwind-variants";
    import { cn } from "$lib/utils";

    let message = "";
    let orders = [];
    let totalBurgers = 0;
    let totalFries = 0;
    let totalDrinks = 0;
    let nextOrderId = 1;
    let showModal = false;
    let errorMessage = "";

    const pageStyles = tv({
        slots: {
            main: "w-[40rem] mx-auto",
            content: cn(
                "my-9 mx-auto max-w-7xl py-3 ",
                "relative isolate overflow-hidden",
                "bg-gray-900 pt-16 shadow-2xl rounded-3xl px-16",
            ),
            section: "mx-auto max-w-md text-left",
            inputWrapper: "mt-6 flex max-w-md gap-x-4 my-3",
        },
    });

    const host = "http://localhost:8000";

    async function handleOnClick(event) {
        event.preventDefault();
        const formData = {
            content: message,
        };

        try {
            const response = await axios.post(host + "/order", formData, {
                headers: {
                    "Content-Type": "application/json",
                },
            });

            const data = response.data;
            console.log(data);

            if (data.order) {
                orders = [
                    ...orders,
                    {
                        orderId: nextOrderId++,
                        burgers: parseInt(data.order.burger || 0),
                        fries: parseInt(data.order.fries || 0),
                        drinks: parseInt(data.order.drink || 0),
                    },
                ];
            } else if (data.cancel) {
                let orderIds = data.cancel;
                if (orderIds.length === 0) {
                    // cancel all orders
                    orders = [];
                } else {
                    // check if all orderIds are valid
                    for (let orderId of orderIds) {
                        if (
                            !orders.find((order) => order.orderId === orderId)
                        ) {
                            throw new Error("Order not found");
                        }
                    }

                    orders = orders.filter(
                        (order) => !orderIds.includes(order.orderId),
                    );
                }
            } else if (data.error) {
                throw new Error(data.error);
            } else {
                throw new Error("Invalid request");
            }
        } catch (error) {
            // alert(error.message);
            errorMessage = error.message;
            showModal = true;
        }
    }

    $: totalBurgers = orders.reduce((total, order) => total + order.burgers, 0);
    $: totalFries = orders.reduce((total, order) => total + order.fries, 0);
    $: totalDrinks = orders.reduce((total, order) => total + order.drinks, 0);
</script>

<main class={pageStyles.slots.main}>
    <div class={pageStyles.slots.content}>
        <div class={pageStyles.slots.section}>
            <TotalSection {totalBurgers} {totalFries} {totalDrinks} />

            <div class={pageStyles.slots.inputWrapper}>
                <Input bind:message />
                <Button variant="custom" size="custom" on:click={handleOnClick}>
                    Run
                </Button>
            </div>

            <OrderHist {orders} />
        </div>
    </div>
</main>
<Modal
    isOpen={showModal}
    message={errorMessage}
    onClose={() => (showModal = false)}
/>

<style>
</style>
