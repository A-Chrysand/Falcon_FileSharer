<template>
	<div class="div_header ">
		<div class="title">
			<h1>{{msg}}</h1>

		</div>
	</div>
	<hr v-if="NeedHr">
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";

@Options({
	props: {
		msg: String,
		NeedHr: Boolean,
	},
})
export default class Title extends Vue {
	msg!: string;
	NeedHr!: boolean;
}
</script>

<style lang="sass">
@import @/components/component
.div_header
	.title
		margin: 1rem 1rem
		display: flex
		@media (max-width:321px)
			margin-left: 0.5rem
	h1,h2,h3
		margin: 0
hr
	opacity: 0.5
	margin: 0
</style>