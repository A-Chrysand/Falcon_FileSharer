<template >
	<div class="hamburger" :class="AsideIsOpen?'h_active':''"
		:style="{'--HambugerWidth':parm_string_width,'--Color':parm_string_color}">
		<span class="line"></span>
		<span class="line"></span>
		<span class="line"></span>
	</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
	name: "HambugerButton",
	data(): any {
		return {
			AsideIsOpen: this.parm_bool_AsideIsOpen,
		};
	},
	props: {
		parm_bool_AsideIsOpen: {
			type: Boolean,
			default: false,
		},
		parm_string_width: {
			type: String,
			default: "50px",
		},
		parm_string_color: {
			type: String,
			default: "black",
		},
	},
	watch: {
		parm_bool_AsideIsOpen() {
			this.AsideIsOpen = this.parm_bool_AsideIsOpen;
		},
	},
});
</script>

<style lang="sass">
/**虽然不正，But也算了 */
$animate_time: 0.08s
$Width: var(--HambugerWidth)
$Height: 5px
$Margin2: calc( #{$Width} / 6.25)
$Margin13: calc( #{$Width} / 13)
.hamburger

	height: $Width
	width: $Width
	cursor: pointer

	.line
		width: 100%
		height: $Height
		display: block

		background-color: var(--Color)
		transition: all $animate_time ease-in-out
		margin: $Margin13
		&:nth-child(2)
			margin: $Margin2 auto

	&.h_active
		transform: rotate(45deg)
		transition: all $animate_time ease-in-out
		transition-delay: $animate_time * 2

		.line
			$MH: calc(#{$Width} / 6.25 + #{$Height})
			$Anti-MH: calc(-1 * (#{$Width} / 6.25 + #{$Height}))

			&:nth-child(2)
				width: 0px
			&:nth-child(1), &:nth-child(3)
				transition-delay: $animate_time

			&:nth-child(1)
				transform: translateY($MH)

			&:nth-child(3)
				transform: translateY($Anti-MH) rotate(90deg)
</style>